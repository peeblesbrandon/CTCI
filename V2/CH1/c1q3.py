def URLify(string, length):
    if length < 3:
        return None
    output = [None] * len(string)
    i, j = 0, 0
    while i < length:
        if string[i] == ' ':
            for x in range(len('%20')):
                output[j] = '%20'[x]
                j += 1
        else:
            output[j] = string[i]
            j += 1
        i += 1
    return ''.join(output)

if __name__ == '__main__':
    test = 'Mr John Smith    '
    print(URLify(test, 13))
    test = ' a b    '
    print(URLify(test, 4))
    test = " a b       "
    print(URLify(test, 5))
