array = [[1, 2, 0], [0, 1, 0], [2, 2, 0]]


# See how many playfields are empty.
def freefields(array):
    strarray = str(array)
    emptyfields = strarray.count("0")
    return emptyfields


print(freefields(array))
