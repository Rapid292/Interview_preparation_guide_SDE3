from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        column = defaultdict(set)
        square = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": # Skip "." in the code
                    continue
                if board[i][j] in row[i]:
                    return False
                row[i].add(board[i][j])

                if board[i][j] in column[j]:
                    return False
                column[j].add(board[i][j])

                if board[i][j] in square[(i//3,j//3)]: # tuple of (i//3, j//3) as key for squre
                    return False
                square[(i//3,j//3)].add(board[i][j])
        return True
