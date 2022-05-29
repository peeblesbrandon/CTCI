def isPalinPerm(str):
    # count freq of each character in string
    charCounts = {} # O(N)
    for char in str: # O(N)
        char = char.lower() # O(1)
        if char.isalpha():  # O(1)
            if char in charCounts:  # O(1)
                charCounts[char] += 1  # O(1)
            else:  # O(1)
                charCounts[char] = 1  # O(1)
    # check that there is at most one odd count in hash table
    hasOdd = False  # O(1)
    for count in charCounts.values():  # O(1)
        if count % 2 != 0:  # O(1)
            if hasOdd is True: # more than one odd char count O(1)
                return False
            hasOdd = True  # O(1)
    return True

if __name__ == "__main__":
    print(isPalinPerm('Tact Coa') is True)
    print(isPalinPerm('reCa Cra') is True)
    print(isPalinPerm('ata9bb') is True)         
    print(isPalinPerm('racecars') is False)


# O(N) time
# O(N) space
        
            
