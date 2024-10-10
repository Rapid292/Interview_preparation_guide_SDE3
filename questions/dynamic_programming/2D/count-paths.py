class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Common mistakes:
        # 1. Not initializing dp array correctly
        # 2. Not iterating over dp array correctly
        # 3. Not using space complexity optimization (using 1D array instead of 2D array)

        # Notes:
        # Time Complexity: O(m * n)
        # - We iterate over the dp array once
        # Space Complexity: O(n)
        # - We use a 1D array of size n to store the number of paths to each cell

        # Approach:
        # 1. Use dynamic programming with a 1D array to store the number of paths to each cell
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pathMap = {}

        def helper(m, n):
            if m == 1 or n == 1:
                return 1

            if (m, n) not in pathMap:
                pathMap[(m, n)] = helper(m-1, n) + helper(m, n-1)

            return pathMap[(m, n)]

        return helper(m, n)

    # Common mistakes:
    # 1. Forgetting to handle the base case (when m or n is 1)
    # 2. Not using memoization, leading to exponential time complexity
    # 3. Incorrectly calculating the number of paths (should be sum of paths from above and left)

    # Notes:
    # Time Complexity: O(m * n)
    # - Each subproblem (m, n) is solved once and memoized
    # - There are m * n possible subproblems

    # Space Complexity: O(m * n)
    # - In the worst case, we store the result for each subproblem in pathMap
    # - The recursion stack can go as deep as m + n, but this is dominated by O(m * n)

    # Approach:
    # 1. Use recursive function with memoization (top-down dynamic programming)
    # 2. Base case: if m or n is 1, there's only one path
    # 3. For other cases, number of paths = paths from above + paths from left
    # 4. Store computed results in pathMap to avoid redundant calculations
    # 5. Return the total number of unique paths for the given m x n grid