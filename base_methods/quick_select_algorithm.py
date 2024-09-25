def quick_select(arr, k):
    """
    Find the kth smallest element in an array.

    Parameters:
        arr (list): The input array.
        k (int): The index of the element to find (1-indexed).

    Example:
        >>> quick_select([5, 2, 8, 3, 1, 6, 4], 3)
        3
    """
    def partition(left, right, pivot_index):
        """
        Move the pivot element to the right position and return its index.

        Parameters:
            left (int): The start index of the partition.
            right (int): The end index of the partition.
            pivot_index (int): The index of the pivot element.

        Example:
            >>> arr = [5, 2, 8, 3, 1, 6, 4]
            >>> partition(0, len(arr) - 1, 0)
            3
            >>> arr
            [2, 1, 3, 5, 4, 6, 8]
        """
        pivot_value = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left
        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index

    def select(left, right, k_smallest):
        """
        Recursively select the kth smallest element.

        Parameters:
            left (int): The start index of the selection.
            right (int): The end index of the selection.
            k_smallest (int): The index of the element to find (0-indexed).

        Example:
            >>> arr = [5, 2, 8, 3, 1, 6, 4]
            >>> select(0, len(arr) - 1, 3)
            3
        """
        if left == right:
            return arr[left]
        pivot_index = partition(left, right, left)
        if k_smallest == pivot_index:
            return arr[k_smallest]
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        else:
            return select(pivot_index + 1, right, k_smallest)

    return select(0, len(arr) - 1, len(arr) - k)

