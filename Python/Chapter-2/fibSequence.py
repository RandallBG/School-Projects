maxNum = int(input("Enter the amount of numbers in fib sequence"))
numberArr = [0]



for i in range(1,maxNum):
    if i > 1:
        numberArr.append(numberArr[i-1] + numberArr[i-2])
        print(i, numberArr[i], numberArr[i-1], numberArr[i-2])
    if i == 1:
        numberArr.append(1)

print(numberArr)

print("Golden Ratio: 1.618034", "Your Ratio:", numberArr[maxNum-1]/ numberArr[maxNum-2])