import random


def count_conflicts(board):
    """Return number of pairwise conflicts on the board."""
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j]:
                conflicts += 1
            elif abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts


def solve_n_queens_hill_climbing(n, max_restarts=100, max_steps=1000):
    """
    Solve N-Queens using Hill Climbing with Random Restarts.

    Returns a solution board (list of row indices) or None if not found.
    """
    def random_board():
        return [random.randint(0, n - 1) for _ in range(n)]

    for _ in range(max_restarts):
        current = random_board()
        current_conflicts = count_conflicts(current)

        for _step in range(max_steps):
            if current_conflicts == 0:
                return current

            best_neighbor = current
            best_conflicts = current_conflicts

            # generate neighbors by moving one queen in each column
            for col in range(n):
                for row in range(n):
                    if row == current[col]:
                        continue
                    neighbor = current[:]
                    neighbor[col] = row
                    c = count_conflicts(neighbor)
                    if c < best_conflicts:
                        best_neighbor = neighbor
                        best_conflicts = c

            # if no improvement, break to restart
            if best_conflicts >= current_conflicts:
                break

            current = best_neighbor
            current_conflicts = best_conflicts

    return None