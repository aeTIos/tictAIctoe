#input board array, move tuple, player int
#output updated board array

gamestate = [[1,2,3],[4,5,6],[7,8,9]]
move = (1,0)
player = 100

def update_board(gamestate, move, player):
    gamestate[move[0]][move[1]] = player
    return gamestate


print(update_board([[1,2,3],[4,5,6],[7,8,9]],move,player))

