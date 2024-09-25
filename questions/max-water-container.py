from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        i, j = 0, len(heights)-1

        while i<j:
            area = (j-i)*min(heights[i], heights[j])
            max_area = max(area, max_area)

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        # Common mistakes:
        # 1. Do not return area directly, instead, compare with max_area and return max_area
        # 2. Do not compare heights[i] and heights[j] directly, instead, compare their min and max
        # 3. Do not forget to increment i or decrement j during the loop

        return max_area

# Notes:
# Time Complexity:
# O(n) - We only traverse the list once with the two pointers moving towards each other.
# Space Complexity:
# O(1) - Only constant extra space is used for variables max_area, i, and j.

# Approach:
# Use two pointers, one at the beginning and one at the end of the list.
# Calculate the area between the two pointers and compare it with the max_area.
# Move the pointer that is pointing to the shorter line towards the other pointer.
# Repeat the process until the two pointers meet.
