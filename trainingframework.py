"""
Aanleveren ([[0,0,0],[0,0,0],[0,0,0]], 1|2)
"""

import stupidbot as bot1
import retardbot as bot2
import random

ROUNDSTOBEPLAYED = 1000


def print_board(board):
    print(' ' + str(board[0][0]) + ' | ' + str(board[0][1]) + ' | ' + str(board[0][2]))
    print('-----------')
    print(' ' + str(board[1][0]) + ' | ' + str(board[1][1]) + ' | ' + str(board[1][2]))
    print('-----------')
    print(' ' + str(board[2][0]) + ' | ' + str(board[2][1]) + ' | ' + str(board[2][2]))
    print('\n')


def choose_starting_player():
    return random.randint(1, 2)


def game_init(def_ar):
    current_array = def_ar
    return current_array


def make_move(board, ap):
    move = (-1, -1)
    try:  # KWARGS gebruikt. Voor betere uitwisselbaarheid van bots.
        if ap == 1:
            move = bot1.move(array=board, speler=ap)
        if ap == 2:
            move = bot2.move(array=board, speler=ap)
    except ValueError:
        print("make_move failed")
        move = (None, None)
    try:
        if move[0] < 0 or move[0] > 2:
            move = (None, None)
        if move[1] < 0 or move[1] > 2:
            move = (None, None)
    except TypeError:
        move = (None, None)
    return move


def flip_player(ap):
    curpl = -1
    try:
        if ap == 1:
            curpl = 2
        if ap == 2:
            curpl = 1
    except ValueError:
        print("flip_player fail")
    return curpl


def check_winner(array):
    if array[0][0] == 1 and array[0][1] == 1 and array[0][2] == 1:
        return 1
    if array[0][0] == 1 and array[1][0] == 1 and array[2][0] == 1:
        return 1
    if array[0][1] == 1 and array[1][1] == 1 and array[2][1] == 1:
        return 1
    if array[0][2] == 1 and array[1][2] == 1 and array[2][2] == 1:
        return 1
    if array[1][0] == 1 and array[1][1] == 1 and array[1][2] == 1:
        return 1
    if array[2][0] == 1 and array[2][1] == 1 and array[2][2] == 1:
        return 1
    if array[0][2] == 1 and array[1][1] == 1 and array[2][0] == 1:
        return 1
    if array[0][0] == 1 and array[1][1] == 1 and array[2][2] == 1:
        return 1

    if array[0][0] == 2 and array[0][1] == 2 and array[0][2] == 2:
        return 2
    if array[0][0] == 2 and array[1][0] == 2 and array[2][0] == 2:
        return 2
    if array[0][1] == 2 and array[1][1] == 2 and array[2][1] == 2:
        return 2
    if array[0][2] == 2 and array[1][2] == 2 and array[2][2] == 2:
        return 2
    if array[1][0] == 2 and array[1][1] == 2 and array[1][2] == 2:
        return 2
    if array[2][0] == 2 and array[2][1] == 2 and array[2][2] == 2:
        return 2
    if array[0][2] == 2 and array[1][1] == 2 and array[2][0] == 2:
        return 2
    if array[0][0] == 2 and array[1][1] == 2 and array[2][2] == 2:
        return 2

    zerosleft = False

    for i in array:
        for number in i:
            if number == 0:
                zerosleft = True
        if zerosleft == False:
            return 0

    # winner is -1, 0, 1, 2
    # -1 Undecided
    # 0 Draw
    # 1, 2 winners
    winner = -1
    return winner


def check_move(move, board, speler):
    correct = True

    try:
        if board[move[0]][move[1]] != 0:
            correct = False
    except (ValueError, TypeError):  # TypeError vangt de (None, None) moves.
        correct = False
    return [correct, move, board, speler]


def insert_move(move, board, player):
    """
    :param move: tuple(boardX, boardY)
    :param board: Nested 3-array
    :param player: player number
    :return: Nested 3-array
    """
    board[move[0]][move[1]] = player
    return board


def play_game(curar, startplr):
    winner = -1
    current_player = flip_player(startplr)
    game_collapsed = False
    while game_collapsed is False:
        current_player = flip_player(current_player)
        move = check_move(make_move(curar, current_player), curar, current_player)
        if move[0] is True:
            curar = insert_move(move[1], move[2], move[3])
            # print_board(curar)
        else:
            curpl = move[3]  # Wissel de speler om, omdat de speler hier de fout in gaat, de ander wint.
            if curpl == 2:
                curpl = 1
            else:
                curpl = 2
            winner = curpl
            break
        winner = check_winner(curar)
        if winner != -1:
            game_collapsed = True
    if winner == -1:
        raise ValueError("Play Game failed")
    else:
        return winner


def main():
    default_array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    games_played = 0
    games_won = (0, 0)

    current_player = choose_starting_player()
    # print("Bot1 = {}\nBot2 = {}".format(str(bot1.__file__).split('/')[-1], str(bot2.__file__).split('/')[-1]))
    p1wins = 0
    p2wins = 0
    # Game loop
    while games_played < ROUNDSTOBEPLAYED:
        current_array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # game_init(default_array)
        winner = play_game(current_array, current_player)
        # print(winner)
        # print("speler {0} heeft gewonnen".format(winner))
        games_played = games_played + 1
        if winner == 1:
            p1wins = p1wins + 1
        if winner == 2:
            p2wins = p2wins + 1
        current_player = flip_player(current_player)
        print("De stand is: {0}-{1} \nSpeler1 heeft {0} punten --- Speler2 heeft {1} punten".format(p1wins, p2wins))


if __name__ == "__main__":
    main()


