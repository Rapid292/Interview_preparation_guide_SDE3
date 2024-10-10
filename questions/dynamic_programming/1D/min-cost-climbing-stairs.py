from typing import List


class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1)

        # Common mistakes:
        # 1. Do not initialize dp array with cost[0] and cost[1] as it will not work for the edge cases.
        # 2. Do not initialize dp array with cost[0] or cost[1] only as it will not work for the edge cases.
        # 3. Do not forget to return dp[n] at the end of the function.

        # Notes:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # Approach: Use dynamic programming to store the minimum cost at each step.

        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Common mistakes:
        # 1. Do not return minCost(0) or minCost(1) as it will not give the correct result.
        # 2. Do not forget to add the cost of the step in the recursive call.
        # 3. Do not forget to add the base case when i >= len(cost).

        # Notes:
        # Time Complexity: O(2^n)
        # Space Complexity: O(n)
        # Approach: Use recursion to find the minimum cost of climbing the stairs.

        def minCost(i):
            if i >= len(cost):
                return 0
            return cost[i] + min(minCost(i+1), minCost(i+2))
        return min(minCost(0), minCost(1))
