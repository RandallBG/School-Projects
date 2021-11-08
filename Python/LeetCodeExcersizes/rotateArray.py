

def rotateArray(nums, k):
    # whoever figured this out is a genius
    n = len(nums)
    k%=n
    nums[:] = nums[n-k:]+nums[:n-k]

numArray = [10,11,12,13,14,15,16,17,18,19,20]

rotateBy = 3

rotateArray(numArray, rotateBy)

print(numArray)