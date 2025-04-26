import numpy as np

def is_valid_sudoku(board):
    def is_valid_block(block):
        block = block.flatten()
        block = block[block > 0]
        return len(block) == len(set(block))
    for row in board:
        if not is_valid_block(row):
            return False
    for col in board.T:
        if not is_valid_block(col):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = board[i:i+3, j:j+3]
            if not is_valid_block(subgrid):
                return False
    return True

#Examples

valid_board = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])
print(is_valid_sudoku(valid_board))

invalid_board = np.array([
    [5, 3, 5, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])
print(is_valid_sudoku(invalid_board))