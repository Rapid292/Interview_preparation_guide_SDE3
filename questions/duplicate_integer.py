from collections import defaultdict
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        # Initialize defaultdict with boolean default which defaults to False
        number_hash = defaultdict(bool)
        for num in nums:
            if number_hash[num]:
                return True
            number_hash[num] = True
        return False

# Time complexity: O(n)