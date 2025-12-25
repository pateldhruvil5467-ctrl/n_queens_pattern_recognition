def solve_n_queens_csp(n):
    """
    Solve N-Queens using Constraint Satisfaction Problem (CSP) approach with forward checking.
    """
    solutions = []

    #Each column has a domain of possible rows

    domains = [set(range(n)) for _ in range(n)]
    board = [-1] * n  # Initialize the board with -1 (no queens placed)

    def is_consistent(col, row):
        for prev_col in range(col):
            prev_row = board[prev_col]
            if prev_row == -1:
                continue
            if prev_row == row:
                return False
            if abs(prev_row - row) == abs(prev_col - col):
                return False
            
                
        return True
    
    def forward_check(col, row, domains_copy):
        # For each future column, remove values that conflict with placing
        # a queen at (col, row). If any domain becomes empty, fail.
        for next_col in range(col + 1, n):
            to_remove = set()
            for r in list(domains_copy[next_col]):
                if r == row or abs(r - row) == abs(next_col - col):
                    to_remove.add(r)
            domains_copy[next_col] -= to_remove
            if not domains_copy[next_col]:
                return False
        return True
    
    def backtrack(col, domains):
          if col == n:
                solutions.append(board.copy())
                return
          
          for row in domains[col]:
                if is_consistent(col, row):
                    board[col] = row
                    new_domains = [d.copy() for d in domains]

                    if forward_check(col, row, new_domains):
                        backtrack(col + 1, new_domains)

                    board[col] = -1  # Reset the position
        
    backtrack(0, domains)
    return solutions

                