import hashlib

#Ubersimple hashing function
def hash(array):
    strarray = str(array)
    input = ''.join(strarray)
    return hashlib.sha256(input.encode('utf-8')).hexdigest()

def getvalidmoves(gamestate):
    availablemoves = []
    for y in range(len(gamestate)):
        for x in range(len(gamestate[y])):
            if gamestate[y][x] == 0:
                coord = (y,x)
                availablemoves.append(coord)
    return availablemoves

