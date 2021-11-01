# # Count by fives

# # create function
# def countByFive(maxNum):
#     for i in range(0, maxNum+1, 5):
#         print(i)


# num = int(input("Enter a number to count to: "))
# countByFive(num)


# determine if palindrome

# def IsPalindrome(checkString):
#     if(checkString == checkString[::-1]):
#         print("This is a palindrome")
#         print(checkString)
#         print(checkString[::-1])
#     else:
#         print("This is not a palindrome")
#         print(checkString)
#         print(checkString[::-1])


# palindrome = input("enter a word or number to check for palindrome: ")
# IsPalindrome(palindrome)


# Total up scores of multiple lists

studentScores = [ "Snoop", [ 89, 78, 88,70, 95 ],  "Omar", [ 88, 88, 85,76, 89], "Stringer", [ 98, 93, 99, 95, 99 ], "Marlo", [ 79, 76, 88, 87, 100]  ]

def studentTotals(scoreList):
    total = 0
    average = 0

    for i in range(0 ,len(scoreList), 2):
        total = 0
        print(scoreList[i])
        for x in range(0, len(scoreList[i+1])):
            total += scoreList[i+1][x]
        average = round(total/ len(scoreList[i+1]))
        print("total:", total)
        print("average", average)


studentTotals(studentScores)