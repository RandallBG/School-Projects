import math

def searchNumArray(nums, target):
  
    low = 0
    high = len(nums) -1
    mid = 0
    
    while low <= high:
        
        mid = (high + low) // 2
        print(nums[mid])

        if nums[mid] > target:
            high = mid -1
        if nums[mid] < target:
            low = mid +1
        if nums[mid] == target:
            return mid
    
    return -1
    
numsArray = [-1, 0, 5, 7, 10, 15, 20, 90]

# print(numsArray[1:2])

print(searchNumArray(numsArray, 11))