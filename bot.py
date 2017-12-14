import functions

#initialise
class Vars:
    def __init__(self):
        self.big_db = functions.load_json('db.json')
        self.movesduringgame = {}




def move(board, player):
    boardhash = functions.gamestate_hash(board)
    possiblemoves = functions.fetch_moves(big_db, boardhash)
    move = functions.generate_move(possiblemoves)
    movesduringgame.update({boardhash: move})
    board = functions.update_board(board, move)
    endgame = functions.game_end(board)

    if endgame in [0,1,2]:
        if endgame == 0:
            # phew, a draw
            adjust = 5
        elif endgame == player:
            # WE WIN!!!!11!!!!
            adjust = 10
        else:
            # WE LOST :((((((
            adjust = -1
        functions.update_database(movesduringgame, big_db, adjust)
        movesduringgame = {} #reset array of played moves

    return move