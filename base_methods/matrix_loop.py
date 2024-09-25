from collections import defaultdict


def isValidSudoku(self, matrix):
    row = defaultdict(set)
    column = defaultdict(set)
    square = defaultdict(set)

    for i in range(9):
        for j in range(9):
            if matrix[i][j] == ".": # Skip "." in the code
                continue