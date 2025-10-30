def minimax(board, depth, is_maximizing):
    # Simple evaluation function
    scores = {'X': 1, 'O': -1, 'Tie': 0}
    
    result = check_winner(board)
    if result is not None:
        return scores[result]
    
    if is_maximizing:
        best_score = -float('inf')
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def check_winner(board):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    if ' ' not in board:
        return 'Tie'
    return None

# Example use:
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
print(minimax(board, 0, True))  # Start with maximizing player

