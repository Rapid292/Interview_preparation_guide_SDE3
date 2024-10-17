"""
Designing Splitwise
Requirements:
The system should allow users to create accounts and manage their profile information.
Users should be able to create groups and add other users to the groups.
Users should be able to add expenses within a group, specifying the amount, description, and participants.
The system should automatically split the expenses among the participants based on their share.
Users should be able to view their individual balances with other users and settle up the balances.
The system should support different split methods, such as equal split, percentage split, and exact amounts.
Users should be able to view their transaction history and group expenses.
The system should handle concurrent transactions and ensure data consistency.
"""
import datetime
from decimal import Decimal
from typing import List, Dict, Union
from abc import ABC, abstractmethod
import threading

class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.groups = []
        self.expenses = []
        self.balances = {}

    def update_profile(self, name: str = None, email: str = None):
        if name:
            self.name = name
        if email:
            self.email = email

    def add_group(self, group):
        self.groups.append(group)

    def add_expense(self, expense):
        self.expenses.append(expense)

    def update_balance(self, user, amount):
        if user in self.balances:
            self.balances[user] += amount
        else:
            self.balances[user] = amount

class Group:
    def __init__(self, group_id: int, name: str, creator: User):
        self.group_id = group_id
        self.name = name
        self.creator = creator
        self.members = [creator]
        self.expenses = []

    def add_member(self, user: User):
        if user not in self.members:
            self.members.append(user)
            user.add_group(self)

    def add_expense(self, expense):
        self.expenses.append(expense)

class SplitStrategy(ABC):
    @abstractmethod
    def split(self, amount: Decimal, participants: List[User]) -> Dict[User, Decimal]:
        pass

class EqualSplitStrategy(SplitStrategy):
    def split(self, amount: Decimal, participants: List[User]) -> Dict[User, Decimal]:
        share = amount / len(participants)
        return {user: share for user in participants}

class PercentageSplitStrategy(SplitStrategy):
    def __init__(self, percentages: Dict[User, float]):
        self.percentages = percentages

    def split(self, amount: Decimal, participants: List[User]) -> Dict[User, Decimal]:
        return {user: amount * (self.percentages[user] / 100) for user in participants}

class ExactSplitStrategy(SplitStrategy):
    def __init__(self, amounts: Dict[User, Decimal]):
        self.amounts = amounts

    def split(self, amount: Decimal, participants: List[User]) -> Dict[User, Decimal]:
        return self.amounts

class Expense:
    def __init__(self, expense_id: int, amount: Decimal, description: str, paid_by: User, group: Group, split_strategy: SplitStrategy):
        self.expense_id = expense_id
        self.amount = amount
        self.description = description
        self.paid_by = paid_by
        self.group = group
        self.split_strategy = split_strategy
        self.participants = []
        self.shares = {}
        self.date = datetime.datetime.now()

    def add_participant(self, user: User):
        self.participants.append(user)

    def split_expense(self):
        self.shares = self.split_strategy.split(self.amount, self.participants)

        for user, share in self.shares.items():
            if user != self.paid_by:
                user.update_balance(self.paid_by, share)
                self.paid_by.update_balance(user, -share)

class SplitwiseSystem:
    def __init__(self):
        self.users = {}
        self.groups = {}
        self.expenses = {}
        self.lock = threading.Lock()

    def create_user(self, name: str, email: str) -> User:
        with self.lock:
            user_id = len(self.users) + 1
            user = User(user_id, name, email)
            self.users[user_id] = user
        return user

    def create_group(self, name: str, creator: User) -> Group:
        with self.lock:
            group_id = len(self.groups) + 1
            group = Group(group_id, name, creator)
            self.groups[group_id] = group
        return group

    def add_expense(self, amount: Decimal, description: str, paid_by: User, group: Group, split_strategy: SplitStrategy, participants: List[User]) -> Expense:
        with self.lock:
            expense_id = len(self.expenses) + 1
            expense = Expense(expense_id, amount, description, paid_by, group, split_strategy)
            
            for user in participants:
                expense.add_participant(user)
            
            expense.split_expense()
            self.expenses[expense_id] = expense
            group.add_expense(expense)
            paid_by.add_expense(expense)

        return expense

    def get_user_balance(self, user: User) -> Dict[User, Decimal]:
        return user.balances

    def settle_balance(self, payer: User, payee: User, amount: Decimal):
        with self.lock:
            payer.update_balance(payee, amount)
            payee.update_balance(payer, -amount)

    def get_user_transaction_history(self, user: User) -> List[Expense]:
        return user.expenses

    def get_group_expenses(self, group: Group) -> List[Expense]:
        return group.expenses


if __name__ == "__main__":

    # Usage example
    system = SplitwiseSystem()

    # Create users
    alice = system.create_user("Alice", "alice@example.com")
    bob = system.create_user("Bob", "bob@example.com")
    charlie = system.create_user("Charlie", "charlie@example.com")

    # Create a group
    group = system.create_group("Trip to Paris", alice)
    group.add_member(bob)
    group.add_member(charlie)

    # Add an expense with equal split
    equal_split_strategy = EqualSplitStrategy()
    expense1 = system.add_expense(
        amount=Decimal("300.00"),
        description="Hotel",
        paid_by=alice,
        group=group,
        split_strategy=equal_split_strategy,
        participants=[alice, bob, charlie]
    )

    # Add an expense with percentage split
    percentage_split_strategy = PercentageSplitStrategy({alice: 50, bob: 30, charlie: 20})
    expense2 = system.add_expense(
        amount=Decimal("100.00"),
        description="Dinner",
        paid_by=bob,
        group=group,
        split_strategy=percentage_split_strategy,
        participants=[alice, bob, charlie]
    )

    # Add an expense with exact split
    exact_split_strategy = ExactSplitStrategy({alice: Decimal("30.00"), bob: Decimal("25.00"), charlie: Decimal("15.00")})
    expense3 = system.add_expense(
        amount=Decimal("70.00"),
        description="Taxi",
        paid_by=charlie,
        group=group,
        split_strategy=exact_split_strategy,
        participants=[alice, bob, charlie]
    )

    # Get user balances
    alice_balance = system.get_user_balance(alice)
    bob_balance = system.get_user_balance(bob)
    charlie_balance = system.get_user_balance(charlie)

    print(f"Alice's balances: {alice_balance}")
    print(f"Bob's balances: {bob_balance}")
    print(f"Charlie's balances: {charlie_balance}")

    # Get group expenses
    group_expenses = system.get_group_expenses(group)
    print(f"Group expenses: {group_expenses}")