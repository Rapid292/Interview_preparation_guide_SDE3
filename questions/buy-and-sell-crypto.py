from typing import List

# Solution 1: Using Single loop keep track of lowest price and max profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Common mistakes:
        # 1. Forgetting to update lowest_price
        # 2. Forgetting to update profit
        # 3. Forgetting to update the initial values of lowest_price and profit
        # 4. Forgetting to return profit

        # Notes:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # Approach:
        # Keep track of lowest price and max profit seen so far, updating them as we iterate through the prices.

        lowest_price = prices[0]
        profit = 0
        for price in prices:
            lowest_price = min(price, lowest_price)
            profit = max(profit, price-lowest_price)

        return profit


# Solution 2: 2 pointers with 2 while loops
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0

        while right < len(prices) and left < right:
            if prices[right] < prices[left]:
                left = right
                right = left + 1
            else:
                while right < len(prices) and prices[right] >= prices[left]:
                    profit = prices[right] - prices[left]
                    max_profit = max(max_profit, profit)
                    right += 1
        return max_profit
