# check permutations
def checkPermutation(a, b):
    if len(a) != len(b):
        return False
    counts = {}
    # increment counts of chars in a
    for i in range(0, len(a)):
        char = a[i]
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    # decrement counts of chars in b
    for i in range(0, len(b)):
        char = b[i]
        if char not in counts:
            return False
        elif counts[char] == 0:
            return False
        counts[char] -= 1
    # check that all counts are 0
    for val in counts.values():
        if val != 0:
            return False
    return True


if __name__ == '__main__':
    print(checkPermutation('puppy', 'ypupp'))
    print(checkPermutation('puppy', 'yuupp'))
