def print_solution(board):
    for row in board:
        for cell in row:
            print('Q' if cell == 1 else '.', end=" ")
        print()


def is_safe(board, row, col, n):
    # Check the current row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, n):
    if col >= n:
        return True

    # Try placing a queen in all rows for the current column
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            # Recur to place the rest of the queens
            if solve_n_queens_util(board, col + 1, n):
                return True

            # Backtrack if placing queen doesn't lead to a solution
            board[row][col] = 0

    return False


def solve_n_queens(n):
    # Initialize the board with 0s (no queens placed)
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist")
        return False

    print_solution(board)
    return True


# Get user input
n = int(input("Enter the value of N (number of queens): "))
solve_n_queens(n)

