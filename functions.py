import hashlib
import json
from copy import deepcopy
import random

# Generate sha256 hash of gamestate
def gamestate_hash(array):
    strarray = str(array)
    return hashlib.sha256(strarray.encode('utf-8')).hexdigest()


# return array with all possible moves
def init_valid_moves(gamestate):
    availablemoves = []
    for y in range(len(gamestate)):
        for x in range(len(gamestate[y])):
            if gamestate[y][x] == 0:
                coord = [(y, x), 100]
                availablemoves.append(coord)
    return availablemoves


# generate a dictionary {HASH: moves} based on an array with gamestates
def generate_database(states):
    dictionary = {}
    for state in states:
        dictionary.update({gamestate_hash(state): init_valid_moves(state)})
    return dictionary


# return False if there is no win condition; else return winning player
def game_end(array):
    length = len(array)
    vals = [1, 2]
    for player in vals:
        diag1 = 0
        diag2 = 0
        for i in range(0, length):
            dir1 = 0
            dir2 = 0
            for j in range(0, length):
                if array[j][i] == player:
                    dir1 += 1
                if array[i][j] == player:
                    dir2 += 1
                if dir1 == 3 or dir2 == 3:
                    return player
            if array[i][i] == player:
                diag1 += 1
            if array[i][length - 1 - i] == player:
                diag2 += 1
            if diag1 == 3 or diag2 == 3:
                return player
    return False


# loads json file and return a dictionary
def load_json(filename):
    with open(filename, 'r') as f:
        jsonfile = json.load(f)
        return jsonfile


# take a dictionary and save it as a json file
def save_json(filename, dictionary):
    with open(filename, 'w') as f:
        json.dump(dictionary, f)


#
def generate_boards(size):
    """
    Generate all games on a size x size board
    """
    array = [[0 for i in range(size)] for i in range(0, size)]
    boards = [deepcopy(array)]
    get_gamestates(size, deepcopy(array), boards, 1, 0)
    return boards


def get_gamestates(size, gamestate, boards, player, iteration):
    """
    Generate all possible boards based on an initial state
    """
    winyn = game_end(gamestate)
    if winyn is False:
        for i in range(0, size):
            for j in range(0, size):
                tempboard = deepcopy(gamestate)
                if tempboard[i][j] == 0:
                    tempboard[i][j] = iteration % 2 + 1
                    if tempboard not in boards:
                        boards.append(tempboard)
                        get_gamestates(size, deepcopy(tempboard), boards, player, iteration + 1)


# fetch array with move statistics from database
def fetch_moves(database, boardhash):
    with open(database, 'r') as f:
        workfile = json.load(f)
        return workfile.get(boardhash)


# generate a move based on the possible moves
def generate_move(inputarray):
    numberarray = inputarray[-1]
    combined_number = 0
    encounterzero = []

    for i in range(0,len(numberarray)):
        if numberarray[i] is 0:
            encounterzero.append(i)
        combined_number += numberarray[i]

    randomnumber = random.randrange(1, combined_number)
    calcnumber = 0
    for i in range(0, len(numberarray)):
        if i not in encounterzero:
            calcnumber += numberarray[i]
            if randomnumber <= calcnumber:
                retarray = inputarray[i]
                return retarray[0], retarray[1]


# update a board array with a move
def update_board(gamestate, move, player):
    gamestate[move[0]][move[1]] = player
    return gamestate


# update the move counters with amount
def update_database(moves, database, amount):
    for boardhash in moves:
        avail_moves = database[boardhash]
        # find the move that we played
        played_move = moves[boardhash]
        # convert this tuple to an array
        played_move = [x for x in played_move]
        print(played_move)
        # match this move with the available moves to see which we need to update
        for i in avail_moves:
            print(i)
            if i[0] == played_move:
                i[1] += amount
        return
