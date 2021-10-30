# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails 
# the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. 
# You should minimize the number of calls to the API.

def isBadVersion(num):
    if num > 13:
        return True
    else:
        return False
    


def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    low = 0
    high = n
       
        
    while low <= high:
        mid = (high + low) // 2
        print(low, high, mid)
        if(isBadVersion(mid)):
            if(isBadVersion(mid-1)):
                high = mid-1
            else:
                return mid
        else:
            if(isBadVersion(mid+1)):
                return mid+1
            else:
                low = mid+1
                
print(firstBadVersion(1))