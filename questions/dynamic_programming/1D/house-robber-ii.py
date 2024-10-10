from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        return max(self.rob_linear(nums[1:]), self.rob_linear(nums[:n-1]))

    def rob_linear(self, nums):
        if len(nums) == 1:
            return nums[0]

        prev_max, curr_max = 0, 0

        for n in nums:
            temp = curr_max
            curr_max = max(n + prev_max, curr_max)
            prev_max = temp
        return curr_max

    # Common mistakes:
    # 1. Forgetting to handle the case when there's only one house
    # 2. Not considering that the houses are in a circle (first and last are adjacent)
    # 3. Incorrectly updating prev_max and curr_max

    # Notes:
    # Time Complexity: O(n)
    # - We iterate through the list of houses twice in the worst case
    # Space Complexity: O(1)
    # - We use only a constant amount of extra space regardless of input size

    # Approach:
    # 1. Handle edge case of single house
    # 2. Use helper function rob_linear for linear house arrangement
    # 3. Solve twice: once excluding first house, once excluding last house
    # 4. Return maximum of the two results to handle circular arrangement


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        maxLootMap = {}

        def maxLoot(i, house):
            if i >= len(house):
                return 0
            if i not in maxLootMap:
                rob = house[i] + maxLoot(i+2, house)
                skip = maxLoot(i+1, house)
                maxLootMap[i] = max(rob, skip)
            return maxLootMap[i]

        # Common mistakes:
        # 1. In the maxLoot function, do not forget to add the base case when i >= len(house).

        # Notes:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # Approach: Use dynamic programming to store the maximum loot at each step.
        loot_start_0 = maxLoot(0, nums[:n-1])
        maxLootMap = {}
        loot_start_1 = maxLoot(0, nums[1:])

        return max(loot_start_0, loot_start_1)
