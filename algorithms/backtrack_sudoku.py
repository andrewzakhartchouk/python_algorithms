import time

def find_empty(sudo, pos):
    for row in range(9):
        for col in range(9):
            if sudo[row][col] == 0:
                pos[0] = row
                pos[1] = col
                return True
    return False


def check_row(sudo, row, num):
    for i in range(9):
        if sudo[row][i] == num:
            return False
    return True


def check_col(sudo, col, num):
    for i in range(9):
        if sudo[i][col] == num:
            return False
    return True


def check_box(sudo, row, col, num):
    boxrow = (row // 3) * 3
    boxcol = (col // 3) * 3
    for i in range(boxrow, boxrow + 3):
        for j in range(boxcol, boxcol + 3):
            if sudo[i][j] == num:
                return False
    return True


def is_safe(sudo, row, col, num):
    if check_row(sudo, row, num) and check_col(sudo, col, num) and check_box(sudo, row, col, num):
        return True
    return False


def solver(sudo):
    pos = [0, 0]

    if not find_empty(sudo, pos):
        return True

    row = pos[0]
    col = pos[1]

    for num in range(1, 10):
        if is_safe(sudo, row, col, num):
            sudo[row][col] = num
            if solver(sudo):
                return True
            sudo[row][col] = 0
    return False


def printer(sudo):
    for i in range(9):
        if not i % 3 and i != 0:
            print("---------------------")
        for j in range(9):
            if not j % 3 and j != 0:
                print("| ", end = "")
            if j == 8:
                print(str(sudo[i][j]))
            else:
                print(str(sudo[i][j]) + " ", end = '')


if __name__ == "__main__":
    sudokuboard = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                   [6, 0, 0, 1, 9, 5, 0, 0, 0],
                   [0, 9, 8, 0, 0, 0, 0, 6, 0],
                   [8, 0, 0, 0, 6, 0, 0, 0, 3],
                   [4, 0, 0, 8, 0, 3, 0, 0, 1],
                   [7, 0, 0, 0, 2, 0, 0, 0, 6],
                   [0, 6, 0, 0, 0, 0, 2, 8, 0],
                   [0, 0, 0, 4, 1, 9, 0, 0, 5],
                   [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    print("Starting board")
    printer(sudokuboard)
    print("Running solver...\n")
    time.sleep(1)

    if solver(sudokuboard):
        print("Solution found")
        printer(sudokuboard)
    else:
        print("No solution")
