# this generates a random move based on the combined value of the array
import random

def generate_move(inputarray):
    # grab number array from input array ( final array )
    numberarray = inputarray[-1]
    #init number that will be the range of tha random
    combined_number = 0
    # encounter zero
    encounterzero = []
    # loop to add up the numbers
    for i in range(0,len(numberarray)):
        if numberarray[i] is 0:
            encounterzero.append(i)
        combined_number += numberarray[i]

    # random number generate
    randomnumber = random.randrange(1, combined_number)
    #iterate trough teh number array again to do calculations
    calcnumber = 0
    for i in range(0,len(numberarray)):
        # add numbers to calc array
        calcnumber += numberarray[i]
        # if array block is in the encounterzero array continue to (back to top of loop)
        for a in encounterzero:
            if a is i:
                continue
        # if random number is higher then the calculated number continue (back to top of loop)
        if randomnumber > calcnumber:
            continue
        # if random number is lower or equal to calculated number create tuple and return the info.
        elif randomnumber <= calcnumber:
            retarray = inputarray[i]
            return (retarray[0], retarray[1])


print(generate_move([[0,2],[1,2],[0,0],[300,0,150]]))

