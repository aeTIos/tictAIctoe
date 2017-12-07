# training framwork voor de bot te trainen

# import bots
import bot

def trainingframe():
    while_true_check = True
    game_ended = False
    # main game loop
    while(while_true_check):
        # dereference array
        array = None
        # maak nieuwe array
        if game_ended is True:
            # dereference array
            array = None
            # maak nieuwe array
            array = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]

    # check if move is valid
        player1 = moveloop(array, bot, player=1)
        # player2 = moveloop(array ,bot2, player=2)

def moveloop(array, bot, playernumber):
    # krijg tuple van Y en X  in die volegorde
    player1 = bot.move(array,playernumber)

    # check if move is valid
    # TODO : iemand moet deze module maken

    # check of er een winnaar is
    # TODO : Iemand moet deze module maken

    # return tuple
    # TODO : return moet nog worden geschreven





# while loop die nonstop loopt totdat uit wordt gezet


# genereer leeg grid.

# vraag player 1 voor y en x in een touple met een call naar move

# check of move valid is

# check of er een winnaar is

# vraag player 2 voor y en x in ee touple met een call naar move

# check of move valid is

# check of er een winnaar is.

# terug naar begin van de loop