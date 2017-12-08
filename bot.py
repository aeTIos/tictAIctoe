import functions

#initialise
big_db = functions.load_json('db.json')
movesduringgame = {}


def main(board, player):
    boardhash = functions.gamestate_hash(board)
    possiblemoves = functions.fetch_moves(big_db, boardhash)
    move = functions.generate_move(possiblemoves)
    board = functions.update_board(board, move)
    endgame = functions.game_end(board)
    if endgame in [1,2]:
        if endgame == player:
            # WE WIN!!!!11!!!!

