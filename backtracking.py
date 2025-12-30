from utils import is_safe
from utils import is_safe

def solve_n_queens(n):
    """
    Solve the N-Queens problem using backtracking.

    :param n: Size of the chessboard (n x n) and number of queens
    :return: A list of solutions, where each solution is represented as a list
             of column indices for each row.
    """
    def backtrack(current_col):
        if current_col == n:
            # Found a valid solution, add a copy of the board to solutions
            solutions.append(board[:])
            return

        for row in range(n):
            board[current_col] = row
            if is_safe(board, current_col):
                backtrack(current_col + 1)
            # No need to explicitly remove the queen; it will be overwritten in the next iteration

    solutions = []
    board = [-1] * n  # Initialize the board with -1 (no queens placed)
    backtrack(0)
    return solutions