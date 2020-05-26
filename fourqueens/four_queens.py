# Check row for any clash with another queen
def check_row(board, row):
    global N
    for i in range(N):
        if board[row][i] == 1:
            return False
    return True


# Check column for any clash with another queen
def check_col(board, col):
    global N
    for i in range(4):
        if board[i][col] == 1:
            return False
    return True


# Check for clashes on each diagonal from the current position
def check_diag(board, row, col):
    global N
    for mod_row, mod_col in ((1, 1), (1, -1), (-1, 1), (-1, -1)):  # Each tuple corresponds to a diagonal direction
        c_row = row
        c_col = col
        while 0 <= c_row < N and 0 <= c_col < N:  # Until its out of bounds, check and increment
            if board[c_row][c_col] == 1:
                return False
            c_row += mod_row
            c_col += mod_col
    return True


# Returns whether the space can have a queen
def is_safe(board, row, col):
    global N
    if check_row(board, row) and check_col(board, col) and check_diag(board, row, col):
        return True
    return False


# The backtracking algorithm
def solve_queens(board, col):
    global N

    if col >= N:
        return True

    for row in range(N):  # Repeat for each position in a row [1, 2, 3, 4]
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_queens(board, col + 1):  # Repeat for each column per row
                return True
            board[row][col] = 0  # Backtrack: Unsuccessful paths remove placed queen
    return False  # If there is no solution, it fails (for pre-entered test cases)


def printer(board):  # A visual interpretation of the matrix
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("♕ ", end=" ")
            else:
                print("⎕ ", end=" ")
        print("\n")


def board_gen(N):  # Generates the N matrix
    empty = []
    for i in range(N):
        empty.append([])
        for j in range(N):
            empty[i].append(0)
    return empty


if __name__ == "__main__":
    """fq_board = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0], ]"""
    N = int(input("Input N for the N-Queens Problem: "))  # The global variable that can adjust the N-Queens problem
    fq_board = board_gen(N)
    print("Thinking...")

    if solve_queens(fq_board, 0):
        print("Solution")
        printer(fq_board)
    else:
        print("No Solution")
