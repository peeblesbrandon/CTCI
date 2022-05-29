# Is Unique
def isUniqueBruteForce(inputString):
    l = len(inputString)
    for i in range(0, l-1):
        for j in range(i+1, l):
            if inputString[i] == inputString[j]:
                return False
    return True
            
# Brute force optimized
def isUniqueBruteForceOptimized(inputString):
    l = len(inputString)
    if l > 128:
        return False
    for i in range(0, l-1):
        for j in range(i+1, l):
            if inputString[i] == inputString[j]:
                return False
    return True

# array lookup
def isUniqueArray(inputString):
    l = len(inputString)
    if l > 128:
        return False
    seen = [False] * 128
    for i in range(0, l):
        charVal = ord(inputString[i])
        if seen[charVal]:
            return False
        seen[charVal] = True
    return True

if __name__ == '__main__':
    print(isUniqueBruteForce('abc'))
    print(isUniqueBruteForce('abcb'))

    print(isUniqueBruteForceOptimized('abc'))
    print(isUniqueBruteForceOptimized('abcb'))

    print(isUniqueArray('abcdefghijk'))
    print(isUniqueArray('abcdefgchijk'))


