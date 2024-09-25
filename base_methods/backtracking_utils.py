def solve_n_queens(n):
    """
    The N-Queens problem is a classic problem of placing N queens on an NxN chessboard
    such that no two queens attack each other. A queen attacks another queen if they are
    in the same row, column, or diagonal.

    Example:

    >>> solve_n_queens(4)
    [['.Q..',  # Row 1, Col 1
      '..Q.',
      'Q...',
      '...Q'],
     ['..Q.',  # Row 2, Col 2
      'Q...',
      '...Q',
      '.Q..']]

    The output is a list of solutions. Each solution is a list of strings, where each
    string represents a row of the board. The '.' character represents an empty cell,
    and the 'Q' character represents a queen.
    """

    def is_not_under_attack(row, col):
        """
        Check if a queen at position (row, col) is not under attack from any other queen.

        A queen is under attack if there is another queen in the same row, column, or
        diagonal. The 'cols' set keeps track of the columns that have a queen in them.
        The 'hills' and 'dales' sets keep track of the diagonals that have a queen in
        them.

        :param row: the row of the position to check
        :param col: the column of the position to check
        :return: True if the position is not under attack, False otherwise
        """
        return not (cols[col] or hills[row - col] or dales[row + col])

    def place_queen(row, col):
        """
        Place a queen at position (row, col) on the board.

        :param row: the row of the position to place the queen
        :param col: the column of the position to place the queen
        """
        queens.add((row, col))
        cols[col] = 1
        hills[row - col] = 1
        dales[row + col] = 1

    def remove_queen(row, col):
        """
        Remove a queen from position (row, col) on the board.

        :param row: the row of the position to remove the queen
        :param col: the column of the position to remove the queen
        """
        queens.remove((row, col))
        cols[col] = 0
        hills[row - col] = 0
        dales[row + col] = 0

    def backtrack(row):
        """
        Recursively try to place a queen in each column of the given row.

        If a queen can be placed in a column, place it and recursively call backtrack
        on the next row. If a queen cannot be placed in any column, backtrack to the
        previous row and try the next column.

        :param row: the row to place the queen in
        """
        for col in range(n):
            if is_not_under_attack(row, col):
                place_queen(row, col)
                if row + 1 == n:
                    add_solution()
                else:
                    backtrack(row + 1)
                remove_queen(row, col)

    def add_solution():
        """
        Add the current solution to the list of solutions.

        A solution is a list of strings, where each string represents a row of the
        board. The '.' character represents an empty cell, and the 'Q' character
        represents a queen.
        """
        solution = []
        for _, col in sorted(queens):
            solution.append('.' * col + 'Q' + '.' * (n - col - 1))
        solutions.append(solution)

    cols = [0] * n
    hills = [0] * (2 * n - 1)
    dales = [0] * (2 * n - 1)
    queens = set()
    solutions = []
    backtrack(0)
    return solutions
