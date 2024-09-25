def binary_search(arr, target):
    """
    Perform a binary search on a sorted array.

    Examples:
        >>> binary_search([1, 3, 5, 7, 9], 5)
        2
        >>> binary_search([1, 3, 5, 7, 9], 6)
        -1
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def search_rotated_sorted_array(arr, target):
    """
    Search for an element in a rotated sorted array.

    Examples:
        >>> search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 0)
        4
        >>> search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 3)
        -1
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# Notes:
# Time Complexity:
# O(log n) - We are halving the search space with each iteration.
# Space Complexity:
# O(1) - Only constant extra space is used for variables left, right, and mid.

# Approach:
# Use modified binary search to handle the rotated sorted array.
# If the left half is sorted, check if the target is in the left half.
# If not, check in the right half.
# If the right half is sorted, check if the target is in the right half.
# If not, check in the left half.
