from copy import deepcopy


def generate_boards(size):

    array = [[0 for i in range(size)] for i in range(0, size)]

    boards = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]]]

    get_states(size, deepcopy(array), boards, 1, 0)

    return boards


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

                        # print('this is a new state!')

                        boards.append(tempboard)
                        # print('appended tempboard to boards!')
                        # print(f'Boards is now:\n {boards}')
                        get_states(size, deepcopy(tempboard), boards, player, iteration + 1)
                    else:
                        pass
                        # print('This state already exists!')
                else:
                    pass

#testarray = [[1,0,2],
#             [0,2,0],
#             [2,1,1]]

#print(win(testarray))
