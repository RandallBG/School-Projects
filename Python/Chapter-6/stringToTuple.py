def stringToTuple(stringToConvert):
    return tuple(map(tuple,stringToConvert))


name = input("enter a string: ")
print(stringToTuple(name))

