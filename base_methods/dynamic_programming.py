def longest_common_subsequence(text1, text2):
    """
    Given two strings text1 and text2, return the length of their longest common subsequence.
    A subsequence of a string is a new string generated from the original string with some
    characters (can be none) deleted without disturbing the relative positions of the remaining characters.
    (eg, "ace" is a subsequence of "abcde" while "aec" is not).

    The longest common subsequence problem is the problem of finding the longest subsequence
    common to all sequences in a set of sequences (often just two sequences). The sequences
    are not required to occupy consecutive positions within the original sequences.

    Example:
        >>> longest_common_subsequence("abcba", "cbad")
        3
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
