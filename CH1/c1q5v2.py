def isOneAway(str1, str2):
    if abs(len(str1) - len(str2)) > 1: # O(1)
        return False
    p1, p2 = 0, 0 # O(1)
    edited = False  # O(1)
    while p1 < len(str1) and p2 < len(str2):  # O(max(S1, S2))
        if str1[p1] != str2[p2]:  # O(1)
            if edited is True:  # O(1)
                return False
            edited = True  # O(1)
            if len(str1) > len(str2):  # O(1)
                p1 += 1  # O(1)
            elif len(str1) < len(str2):  # O(1)
                p2 += 1  # O(1)
            else:
                p1 += 1  # O(1)
                p2 += 1  # O(1)
        else:
            p1 += 1  # O(1)
            p2 += 1  # O(1)
    return True

if __name__ == '__main__':
    print(isOneAway('pale', 'ple') == True) 
    print(isOneAway('bake', 'false') == False)
    print(isOneAway('stopsign', 'topsign') == True)
            
# O(max(S1, S2)) time
# O(1) space