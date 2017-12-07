from functions import hash, getvalidmoves
from bot import generate_boards

# Generate all possible hashes.

def dictgen(states):
    dictionary = {}
    for state in states:
        dictionary.update({hash(state): getvalidmoves(state)})
    return dictionary

print(dictgen(generate_boards(3)))