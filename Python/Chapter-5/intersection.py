def intersect(list1, list2):
    intersectingList = []
    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            if list1[i] == list2[j]:
                intersectingList.append(list1[i])
                continue
    return intersectingList

nums1 = [10, 20, 30 , 40, 50, 60]
nums2 = [30, 40, 52, 50, 22, 43]

nums3 = intersect(nums1, nums2)

print(nums3)