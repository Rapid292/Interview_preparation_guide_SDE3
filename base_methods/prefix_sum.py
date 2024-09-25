def prefix_sum_array(arr):
    """
    Given an array, compute its prefix sum array.

    The prefix sum array is an array where each element is the sum of all elements up to that index in the original array.

    For example, if the input array is [1, 2, 3, 4, 5], the prefix sum array would be [1, 3, 6, 10, 15].

    This can be useful for quickly computing the sum of any subarray within the original array.
    """
    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]
    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    return prefix_sum
