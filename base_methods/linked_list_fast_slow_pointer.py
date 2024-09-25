class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    """
    Checks if a linked list has a cycle.

    :param head: The head of the linked list.
    :return: True if the linked list has a cycle, False otherwise.

    Examples:

    >>> has_cycle(ListNode(1, ListNode(2, ListNode(3, ListNode(1)))))
    True
    >>> has_cycle(ListNode(1, ListNode(2, ListNode(3))))
    False
    """
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
