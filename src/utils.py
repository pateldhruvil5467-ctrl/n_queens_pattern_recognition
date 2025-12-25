def is_safe(board, current_col):
    """
    check whether the queen placed at board[current_col] is safe from attacks

    """
    for previous_col in range(current_col):
        # Check same row and diagonal attacks
        if (board[previous_col] == board[current_col] or
                abs(board[previous_col] - board[current_col]) == abs(previous_col - current_col)):
            return False
    return True
