HowManyTests = int(input("How many tests to enter?"))
testScores = list()
totalScore = 0


for i in range(0, HowManyTests):
    print(i)
    testScores.append(int(input("Enter Test Score #"+ str(i + 1) + " ")))
    totalScore += testScores[i]

average = totalScore / len(testScores)

print(round(average))