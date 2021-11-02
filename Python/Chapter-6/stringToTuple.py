def stringToTuple(stringToConvert):
    for i in range(0,len(stringToConvert)):
        result = tuple(map(tuple, stringToConvert))
        
    return result


name = "cleveland codes"
print(stringToTuple(name))