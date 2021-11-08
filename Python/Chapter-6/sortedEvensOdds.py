def sortList    (listToSort):
    evensList = []
    oddsList = []
    listToSort.sort()
    print(listToSort)
    for i in range(0, len(listToSort)):
        if listToSort[i] % 2 == 0:
            evensList.append(listToSort[i])
        else:
            oddsList.append(listToSort[i])
        
    return (evensList, oddsList)



nums1 = [1,23,12,14,9,8,44]

print(sortList(nums1))