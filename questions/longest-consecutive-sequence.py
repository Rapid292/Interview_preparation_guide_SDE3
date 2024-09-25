from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest


# Time: O(n)

#Note:
# 1. Set is used to check if a number is present in the list in O(1) time. so cnvert list to set of unique numbers
# 2. Just find start of sequence i.e. (num - 1) not in numSet and then keep on increasing length till (num + length) is in numSet.
# 3. Keep track of longest sequence length.