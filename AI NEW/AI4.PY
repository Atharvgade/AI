def solve_n_queens(n):
    # Check if placing a queen at (row, col) is safe
    def is_safe(board, row, col):
        for i in range(row):
            # Check if the same column or same diagonal already has a queen
            if board[i] == col or abs(board[i] - col) == row - i:
                return False
        return True

    # Recursive backtracking function
    def backtrack(row):
        if row == n:
            # All queens are placed successfully
            solutions.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col  # Place queen
                backtrack(row + 1)  # Recurse to place next queen
                board[row] = -1  # Backtrack

    solutions = []
    board = [-1] * n  # Initialize board with -1 (no queens placed)
    backtrack(0)

    # Format solutions: convert board positions into string representation
    return [["." * c + "Q" + "." * (n - c - 1) for c in sol] for sol in solutions]

# Example usage
n = 4
solutions = solve_n_queens(n)

# Print the total number of solutions and each solution
print(f"Total solutions for {n}-Queens: {len(solutions)}")
for solution in solutions:
    print("\n".join(solution))
    print()
