def listAddition(*args: list[int]) -> list:
    
    finalList = []
    for i in range(0, len(args)):
        if len(args[i]) > len(finalList):
            finalList = [0] * len(args[i])
    for i in range(0, len(args)):
        for j in range(0, len(args[i])):
            finalList[j] += args[i][j]
    return finalList




nums1 = [10, 20, 30 , 40, 50, 60]
nums2 = [30, 40, 52, 50, 22, 43]
nums3 = [100,100,100,100]
addedNums = listAddition(nums1, nums2, nums3)

print(addedNums)
