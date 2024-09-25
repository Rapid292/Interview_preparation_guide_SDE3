def dfs_matrix(matrix, i, j, visited):
    """
    Performs a depth-first search on the given matrix, starting at the given cell.

    Approach:
    1. Check if the current cell is out of bounds or has been visited or has a value of 0.
    2. If the cell is valid, mark it as visited and add it to the visited set.
    3. Explore the four adjacent cells in the directions of right, down, left, and up.
    4. Recursively call the dfs_matrix function on each adjacent cell.

    Example:
        >>> matrix = [
        ...     [1, 1, 1, 1, 1],
        ...     [1, 0, 0, 0, 1],
        ...     [1, 0, 1, 0, 1],
        ...     [1, 0, 0, 0, 1],
        ...     [1, 1, 1, 1, 1]
        ... ]
        >>> visited = set()
        >>> dfs_matrix(matrix, 0, 0, visited)
        >>> visited == {(0, 0), (0, 1), (0, 3), (0, 4), (1, 0), (1, 4), (3, 0), (3, 4), (4, 0), (4, 1), (4, 3), (4, 4)}
        True

    :param matrix: The matrix to search.
    :param i: The row index of the starting cell.
    :param j: The column index of the starting cell.
    :param visited: A set of visited cells.
    """
    if (i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or
        (i, j) in visited or matrix[i][j] == 0):
        return
    visited.add((i, j))
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for direction in directions:
        ni, nj = i + direction[0], j + direction[1]
        dfs_matrix(matrix, ni, nj, visited)

# Some common problems that can be solved using DFS on a matrix include:
# 1. Finding the number of connected components in a matrix.
# 2. Finding the size of the largest connected component in a matrix.
# 3. Finding all connected components in a matrix.
# 4. Finding if there is a path from one cell to another in a matrix.
# 5. Finding the shortest path from one cell to another in a matrix.
# 6. Finding the number of islands in a matrix.
# 7. Finding the number of distinct colors in a matrix.
# 8. Finding the number of connected cells with the same color in a matrix.

