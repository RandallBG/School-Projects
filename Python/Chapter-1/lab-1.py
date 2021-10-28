number = 0
numberArr = []
maximum = ''
minimum = ''

while number != -999:
    number = int(input("Enter a number (-999 to exit)"))
    if number != -999:
        if minimum == '':
            minimum = number
        if maximum == '':
            maximum = number
        if number < minimum :
            minimum = number
        if number > maximum:
            maximum = number    
        numberArr.append(number)

print("Maximum", maximum, "\nMinimum", minimum, "Numbers entered: ", len(numberArr))

    

