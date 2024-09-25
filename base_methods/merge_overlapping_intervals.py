def merge_intervals(intervals):
    """
    Merge overlapping intervals in a list of intervals.

    Example:
        >>> merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])
        [[1, 6], [8, 10], [15, 18]]

        >>> merge_intervals([[1, 3], [9, 20], [8, 10], [15, 18]])
        [[1, 3], [8, 20]]

    :param intervals: List of intervals, where each interval is a list of two integers.
    :return: List of merged intervals.
    """
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged
