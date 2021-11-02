def updateTuple(theTuple, indexToChange, changeTo):
    newArray = []
    for i in range(0, len(theTuple)):
        newArray.append(theTuple[i])
    newArray[indexToChange] = changeTo

    return tuple(newArray)



names = ("Randy", "Derek", "Matt", "Sharon", "Jessy")

print(names)

print(updateTuple(names,1,"DORK"))
