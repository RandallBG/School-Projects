# def rotateArray(nums, k):

#     x = 0
#     while x < k:
#         print(x, k)
#         for i in range(len(nums)-1, -1, -1):  
#             print(i)
#             if i+1 > len(nums)-1:
#                 tmp = nums[i]
                    
#             nums[i] = nums[i-1] 
                
#             if i == 0:
#                 nums[i] = tmp
                    
#     x += 1


def rotateArray(nums, k):
    # whoever figured this out is a genius
    n = len(nums)
    k%=n
    nums[:] = nums[n-k:]+nums[:n-k]

numArray = [10,11,12,13,14,15,16,17,18,19,20]

rotateBy = 3

rotateArray(numArray, rotateBy)

print(numArray)