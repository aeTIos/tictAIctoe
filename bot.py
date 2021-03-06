import functions
from copy import deepcopy

#initialise

helpineedtoinitthis = {}
functions.save_json(f'/tmp/moves', helpineedtoinitthis)

helpineedtoinitthis = {'freefields' : 15}

functions.save_json('/tmp/freefields', helpineedtoinitthis)


def move(array, speler):
    DRAWADJUST = 100
    WINADJUST = 1000000000
    LOSEADJUST = -1


    board = array
    player = speler

    # init moves during game
    movesduringgame = functions.load_json(f'/tmp/moves')

    big_db = functions.load_json('db.json')

    freefields = functions.free_fields(deepcopy(board))

    # did we lose when the other side moved?
    ff_json = functions.load_json(f'/tmp/freefields')

    count = ff_json['freefields']
   # print(f'SAVED FREE FIELDS: {count}')
   # print(f'CURRENT FREE FIELDS: {freefields}') 
    
    if freefields > count:
        #we lost :(
        adjust = LOSEADJUST
        functions.update_database(movesduringgame, big_db, adjust)
        functions.save_json('db.json', big_db)
        movesduringgame = {}



    boardhash = functions.gamestate_hash(board)
    # print('\n\n<BOT> BOARD HASH', str(boardhash))

    # print('BH NOT IN BIG DB:')
    # print(boardhash not in big_db)
    if boardhash not in big_db:
        # print('inverting board')
        board = functions.invert_board(deepcopy(board))
        # print(board)
        player = 2 if player == 1 else 1
        boardhash = functions.gamestate_hash(board)
        # print('<BOT> str2' + str(boardhash))


    possiblemoves = functions.fetch_moves(big_db, boardhash)
    # print('<BOT>' + str(possiblemoves))

    newmove = functions.generate_move(possiblemoves)

    movesduringgame.update({boardhash: [newmove[0], newmove[1]]})
    # print()
    # print('<BOT> mdg ' + str(movesduringgame))
    # print('<BOT> bh ' + str(boardhash))

    board = functions.update_board(board, newmove, player)

    endgame = functions.game_end(board)

    if endgame in [3, 1, 2]:
        if endgame == 3:
            # phew, a draw
            adjust = DRAWADJUST
        elif endgame == player:
            # WE WIN!!!!11!!!!
            adjust = WINADJUST
        else:
            # WE LOST :((((((
            adjust = LOSEADJUST
        # print(big_db)
        # print('<BOT> bigdb (noup)'+str(big_db))
        # print('<BOT> mdg  '+str(movesduringgame))
        functions.update_database(movesduringgame, big_db, adjust)
        # print('<BOT> bigdb  '+str(big_db))

        functions.save_json('db.json', big_db)
        movesduringgame = {} # reset array of played moves


    # detect if we draw or lose next turn
    free = functions.free_fields(board)
    
    freefields = {'freefields': free}
    if free == 1:

        emp_field = [-1,-1]
        for y in range(len(board)):
            for x in range(len(board)):
                if board[y][x] == 0:
                    emp_field = [y, x]
        # fill it with the opposing player's number
        opp_player = 2 if player == 1 else 1
        board = functions.update_board(deepcopy(board), emp_field, opp_player)
        endgame = functions.game_end(board)
        if endgame == 3:
            adjust = DRAWADJUST
        elif endgame == opp_player:
            adjust = LOSEADJUST
        functions.update_database(movesduringgame, big_db, adjust)
        functions.save_json('db.json', big_db)
        movesduringgame = {}
        freefields={'freefields': 15}  
    
    functions.save_json(f'/tmp/freefields', freefields)


    # write movesduringgame out to file
    functions.save_json(f'/tmp/moves', movesduringgame)

    # # print('<BOT> newmv  '+str(newmove))

    # print(f'<BOT>  {type(newmove)}, {type(newmove[0])}, {type(newmove[1])}\n\n\n\n')
    return newmove





# board = [[0,0,0],[0,0,0],[0,0,0]]
# player = 0
# while True:
#     end = functions.game_end(board)
#     ## print(end)
#     if end is not False:
#      #   # print(['_', '    p1 wins', '    p2 wins','    draw'][end])
#         board = [[0,0,0],[0,0,0],[0,0,0]]
#
#
#     ## print(board)
#     played_move = move(deepcopy(board),player+1)
#     ## print(f'    player {player+1} plays:')
#     ## print('    ' + str(played_move))
#     board = functions.update_board(deepcopy(board), played_move, player+1)
#     player = abs(player-1)


