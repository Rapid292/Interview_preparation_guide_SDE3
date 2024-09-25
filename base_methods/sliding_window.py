def max_sum_subarray_k(arr, k):
    """
    Given an array and an integer k, find the maximum sum of a subarray of size k.

    Examples:
        >>> max_sum_subarray_k([1, 2, 3, 4, 5], 3)
        14
        >>> max_sum_subarray_k([1, -1, 5, -2, 3], 4)
        7
    """
    max_sum = float('-inf')
    window_sum = 0
    for i in range(len(arr)):
        window_sum += arr[i]
        if i >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[i - (k - 1)]
    return max_sum
