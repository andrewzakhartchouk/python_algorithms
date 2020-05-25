N = 4


# Check row for any clash with another queen
def check_row(board, row):
    for i in range(4):
        if board[row][i] == 1:
            return False
    return True


# Check column for any clash with another queen
def check_col(board, col):
    for i in range(4):
        if board[i][col] == 1:
            return False
    return True


def check_diag(board, row, col):
    for mod_row, mod_col in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
        c_row = row
        c_col = col
        while 0 <= c_row < 4 and 0 <= c_col < 4:
            if board[c_row][c_col] == 1:
                return False
            c_row += mod_row
            c_col += mod_col
    return True


def is_safe(board, row, col):
    if check_row(board, row) and check_col(board, col) and check_diag(board, row, col):
        return True
    return False


def solve_queens(board, col):
    global N

    if col >= N:
        return True

    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_queens(board, col+1):
                return True
            board[row][col] = 0
    return False


if __name__ == "__main__":
    fq_board = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0], ]
    print(fq_board)
    if solve_queens(fq_board, 0):
        print(fq_board)
    else:
        print("No Solution")
