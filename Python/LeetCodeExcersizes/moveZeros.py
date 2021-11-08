# Given an array of numbers move all zeros to the end of the array while preserving the position of the rest of 
# numbers. Do not make a copy of the array to solve this.

#not very efficient
def moveZeros(nums):
    isDone = False
   
    while isDone == False:
        counter = 0
        for i in range(0, len(nums)-1):
                if nums[i] == 0 and nums[i+1] !=0:
                    nums[i] = nums[i+1]
                    nums[i+1] = 0
                    counter += 1
        if counter == 0:
            isDone = True
    
numArray = [1,0,1, 0, 10 ,11]
moveZeros(numArray)

print(numArray)