from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # A dictionary to store the index of each number

        for i, num in enumerate(nums):
            complement = target - num  # The number we need to find
            if complement in num_map:
                # Found the complement, return the indices
                return [num_map[complement], i]
            num_map[num] = i  # Store the number and its index

        return []  # In case there's no valid pair (though the problem guarantees one)
