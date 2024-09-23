from collections import defaultdict
from typing import List

# Solution 1: Using Prefix and Suffix Products
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the result array with 1
        res = [1] * len(nums)

        # Calculate prefix products
        prefix_product = 1
        for i in range(len(nums)):
            res[i] = prefix_product
            prefix_product *= nums[i]

        # Calculate suffix products and multiply with prefix products
        suffix_product = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix_product
            suffix_product *= nums[i]

        return res

# Solution 2: Using Division
class Solution:
    @staticmethod
    def arr_product(arr):
        product = 1
        for num in arr:
            product = product * num
        return product

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = []
        hashmap = defaultdict(int)
        for i, num in enumerate(nums):
            future = nums[i+1:]
            product = Solution.arr_product(prev+future)
            hashmap[i] = product # handle edge case -> [0, 0]
            prev.append(num)

        res = list(hashmap.values())

        return res

