class Solution:
    def threeSum(self, nums):
        target = 0
        final_res = []
        nums = sorted(nums) # time complexity - O(nlogn)
        i = 0
        while i < len(nums)-2: # run loop till 2nd last element # time complexity - O(n^2)
            left, right = i+1, len(nums)-1
            while left < right: # time complexity - O(n)
                curr_sum = nums[left] + nums[right] + nums[i]
                if target < curr_sum:
                    right -= 1
                elif target > curr_sum:
                    left += 1
                elif target == curr_sum:
                    final_res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
            i += 1
        return final_res

# time_complexity = "O(n^2)"
# space_complexity = "O(1)"

# Notes:
# 1. Avoid creating twoSum method as it will make things more complex.
# 2. Write twoSum 2 pointer approach directly.
# 3. Avoid slicing of list in loops as it will create new list each time that uses more memory.