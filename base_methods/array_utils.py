def reverse_array(arr):
    """
    Reverses an array in place.

    Examples:
        >>> reverse_array([1, 2, 3])
        [3, 2, 1]
    """
    return reversed(arr)

def rotate_array(arr, k):
    """
    Rotate an array by k steps.

    Examples:
        >>> rotate_array([1, 2, 3, 4, 5], 2)
        [4, 5, 1, 2, 3]
    """
    k = k % len(arr)
    return arr[-k:] + arr[:-k]
