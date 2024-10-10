from typing import List

def rob(nums):
    prev_max = 0  # Maximum amount of money robbed up to two houses back
    curr_max = 0  # Maximum amount of money robbed up to the previous house

    for num in nums:
        # Store the current maximum before updating
        temp = curr_max

        # Calculate the new maximum:
        # Either rob this house and add to prev_max, or skip it and keep curr_max
        curr_max = max(prev_max + num, curr_max)

        # Update prev_max for the next iteration
        prev_max = temp

    # Return the maximum amount that can be robbed
    return curr_max

# Time Complexity: O(n), where n is the number of houses
# - We iterate through the list of houses once

# Space Complexity: O(1)
# - We use only a constant amount of extra space (prev_max, curr_max, temp)
# regardless of the input size

# Approach:
# This solution uses dynamic programming with constant space to solve the House Robber problem.
# 1. We use two variables (prev_max and curr_max) to keep track of the maximum loot
# 2. For each house, we decide whether to rob it or skip it based on which action maximizes the loot
# 3. We update our variables after each decision
# 4. This approach avoids recursion and uses only constant extra space
# 5. The final result in curr_max represents the maximum amount that can be robbed


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # Dictionary to store already calculated results for each index
        maxAmountCalculated = {}

        def maxAmount(i):
            # If we've already calculated the result for this index, return it
            if i in maxAmountCalculated:
                return maxAmountCalculated[i]

            # Base case: if we've gone past the last house, return 0
            if i >= n:
                return 0

            # Calculate the maximum amount if we rob the current house
            # We add the value of the current house and skip the next one
            rob_house = nums[i] + maxAmount(i + 2)

            # Calculate the maximum amount if we skip the current house
            # We move to the next house without taking anything
            skip_house = maxAmount(i + 1)

            # Store and return the maximum of the two options
            maxAmountCalculated[i] = max(rob_house, skip_house)
            return maxAmountCalculated[i]

        # Start the recursion from the first house (index 0)
        return maxAmount(0)

    # Time Complexity: O(n)
    # - Each house is only calculated once due to memoization
    # - The results are stored and reused, avoiding redundant calculations

    # Space Complexity: O(n)
    # - We use a dictionary to store results for each index
    # - The recursion stack can go as deep as the number of houses in the worst case

    # Approach:
    # This solution uses recursion with memoization to efficiently solve the House Robber problem.
    # 1. For each house, we consider two options:
    #    a. Rob the current house and skip the next one
    #    b. Skip the current house and move to the next one
    # 2. We use memoization (maxAmountCalculated dictionary) to store and reuse calculated results
    # 3. This avoids redundant calculations, significantly improving the time complexity
    # 4. The function returns the maximum amount that can be robbed without choosing adjacent houses