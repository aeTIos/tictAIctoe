from copy import deepcopy


#def generate_moves(gamestates):
#    states = []
#    # generate_moves returns an array of moves
#    for state in gamestates: # state is a 2 dimensional array
#        print(state)
#        for i in range(0, len(state)):
#            for j in range(0, len(state)):
#                if state[i][j] == 0:
#                    placeholder = state
#                    placeholder[i][j] = 1
#
#                    print('\n\n', placeholder, '\n', state)
#                    states.append(placeholder)
#
#    return states
#
#
#round_0 = [[[0, 0],
#           [0, 0]]]
#
#round_1 = generate_moves(round_0)
##round_2 = generate_moves(round_1)
##round_3 = generate_moves(round_2)
#
#print(round_1)
#


def generate_boards(size):

    array = [[0 for i in range(size)] for i in range(0, size)]

    boards = []

    get_states(size, deepcopy(array), boards, 1, 0)

    print(f'\n\n\n{boards}')
    print(len(boards))

#
#def generate_moves(gamestates): # gamestates is a list of.. gamestates. v
#    # generate_moves returns an array of moves
#    for state in gamestates: # state is a 2 dimensional array
#        for i in range(0, len(state)):
#            for j in range(0, len(state)):
#
#
#    # generate all possible next moves from this array
#


def win(array):
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

def get_states(size, array, boards, player, iteration):
    winyn = win(array)
    if winyn is False:
        for i in range(0, size):
            for j in range(0, size):


                tempboard = deepcopy(array)



  #              print(f'\n\nTempboard at start of iteration: {tempboard}\n iter {i} {j}. Step: {iteration}')
 #               print(f'We are going to try position {i}, {j}')

                if tempboard[i][j] == 0:
#                    print('this is a valid move!')

                    tempboard[i][j] = iteration % 2 + 1

  #                  print(f'tempboard is now: \n {tempboard}')
 #                   print(f'The existing boards are: \n {boards}')

                    if tempboard not in boards:

                        #print('this is a new state!')

                        boards.append(tempboard)
                        #print('appended tempboard to boards!')
                        #print(f'Boards is now:\n {boards}')
                        get_states(size, deepcopy(tempboard), boards, player, iteration + 1)
                    else:
                        pass
                        #print('This state already exists!')
                else:
                    pass
                    #print('this is not a valid move!')

                #print(f'trying next state... {iteration}')
    else:
        print(f'We\'ve got a win condition!\n {array} \n The winner is player {winyn}\n')



#testarray = [[1,0,2],
#             [0,2,0],
#             [2,1,1]]

#print(win(testarray))

generate_boards(3)






