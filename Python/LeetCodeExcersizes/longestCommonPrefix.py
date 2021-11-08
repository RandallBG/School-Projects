def longestCommonPrefix(strs):

    
    commonPrefix = ""
    smallestCount = 0
    for x in range(0, len(strs)):
        if len(strs[x]) < len(strs[smallestCount]):
            smallestCount = x
    for i in range(0, len(strs[smallestCount])):
        print("i:", i)
        isCommonPrefix = True
        for j in range(1,len(strs)):
            print("j:",j)
            print("Comparing:", strs[0][i], strs[j][i])
            if strs[0][i] != strs[j][i]:
                isCommonPrefix = False
                    
        if isCommonPrefix == False:
            return commonPrefix
        else:
            commonPrefix += strs[0][i]
    return commonPrefix



stringArray = ["hi", "hilloSir", "hippo", "hillo"]

print(longestCommonPrefix(stringArray))