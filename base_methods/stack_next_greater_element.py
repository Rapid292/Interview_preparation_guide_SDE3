def next_greater_elements(arr):
    """
    Given an array, find the next greater element for each element in the array.
    The next greater element for an element x is the first greater element on the right side of x in array.
    Elements for which no greater element exist, consider next greater element as -1.

    Examples:
        >>> next_greater_elements([4, 5, 2, 25])
        [5, 25, 25, -1]
    """
    stack, result = [], [-1] * len(arr)
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result
