def rotateArray(nums, k):
    
    # only works if k is not larger than array itself
    
    # counter = 0

    # for i in range(len(nums)-k, len(nums)):
    #     nums.insert(counter, nums[i + counter])
    #     counter += 1
    # del nums[-k:k and None]


    i = 0
    tempStorage = nums[0]
    while i <= k:
        for i in range(0, len(nums)):
            if i+1 < len(nums)-1:
                tempStorage = nums[i+1]
                nums[i+1] = nums[i]
            
            
    
    

numArray = [1,2,3,4,5,6,7,8,9]

print(numArray)
rotateArray(numArray, 4)
print(numArray)