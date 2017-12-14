# update the database for played moves with new values by amount
def update_database(moves, database, amount):
    # moves holds all the moves made this game.
    # database holds the entire database

    # iterate trough moves find move in database each iteration and edit locaiton
    for move in moves:
        # if database contains move
        temp = database[move]
        temp[1] += amount
        database[move] = temp
        print(database[move])



    # pass

moves= {"abc" :[None, 1] }
database = {"cdb" : [None, 1], "abc" : [None, 1]}
amount = 5
update_database(moves, database, amount)
print(database)