from functions import hash, getvalidmoves

# Generate all possible hashes.

def dictgen(states):
    dictionary = {}
    for state in states:
        dictionary.update({hash(state): getvalidmoves(state)})
    return dictionary