from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i < j: # 2 pointers
            if target < numbers[i] + numbers[j]:
                j -= 1
            elif target > numbers[i] + numbers[j]:
                i += 1
            else:
                return [i+1, j+1]

# Note: Time: O(n) because of binary search
# Conditions of Question:
# 1. Sorted Array
# 2. Unique Solution
# 3. 1 based index
# 4. Only 1 solution exists
# 5. Space Complexity: O(1)