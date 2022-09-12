import copy
from reversi.constants import COLOR_WHITE, COLOR_BLACK, DEPTH

def bestMove(board):
    best_score = float("-inf")
    best_move = (-1, -1)
    valid_moves = board.get_valid_moves(COLOR_WHITE)
    for move in valid_moves:
        board_copy = copy.deepcopy(board)
        board_copy.make_move(move[0], move[1], COLOR_WHITE)
        # score = minimax(board_copy, DEPTH, False) # Minimax
        score = alpha_beta(board_copy, DEPTH, float("-inf"), float("inf"), False) # Poda alfa-beta
        if (score > best_score):
            best_score = score
            best_move = move
    return best_move

def minimax(board, depth, maximizing_player):
    if (depth == 0 or board.winner() != None):
        return board.evaluate()

    if (maximizing_player):
        best_score = float("-inf")
        valid_moves = board.get_valid_moves(COLOR_WHITE)
        for move in valid_moves:
            board_copy = copy.deepcopy(board)
            board_copy.make_move(move[0], move[1], COLOR_WHITE)
            score = minimax(board_copy, depth - 1, False)
            best_score = max(score, best_score)
        return best_score

    else:
        best_score = float("inf")
        valid_moves = board.get_valid_moves(COLOR_BLACK)
        for move in valid_moves:
            board_copy = copy.deepcopy(board)
            board_copy.make_move(move[0], move[1], COLOR_BLACK)
            score = minimax(board_copy, depth - 1, True)
            best_score = min(score, best_score)
        return best_score

def alpha_beta(board, depth, alpha, beta, maximizing_player):
    if (depth == 0 or board.winner() != None):
        return board.evaluate()

    if (maximizing_player):
        best_score = float("-inf")
        valid_moves = board.get_valid_moves(COLOR_WHITE)
        for move in valid_moves:
            board_copy = copy.deepcopy(board)
            board_copy.make_move(move[0], move[1], COLOR_WHITE)
            score = alpha_beta(board_copy, depth - 1, alpha, beta, False)
            best_score = max(score, best_score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best_score

    else:
        best_score = float("inf")
        valid_moves = board.get_valid_moves(COLOR_BLACK)
        for move in valid_moves:
            board_copy = copy.deepcopy(board)
            board_copy.make_move(move[0], move[1], COLOR_BLACK)
            score = alpha_beta(board_copy, depth - 1, alpha, beta, True)
            best_score = min(score, best_score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score