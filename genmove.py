# this generates a random move based on the combined value of the array
import random

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
                return (retarray[0], retarray[1])

# while(True):
  #  print(generate_move([[0,2],[1,2],[0,0],[300,0,150]]))

