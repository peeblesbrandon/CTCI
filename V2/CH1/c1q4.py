def palindromePermutation(input):
    counts = {}
    for char in input.lower():
        if char != ' ':
            if char not in counts:
                counts[char] = 0
            counts[char] += 1
    
    hasOdd = False
    for val in counts.values():
        if val % 2 == 1:
            if hasOdd:
                return False
            hasOdd = True
    return True

if __name__ == '__main__':
    print(palindromePermutation('racecar'))
    print(palindromePermutation('Taco Coa'))
    print(palindromePermutation('taco dog'))
