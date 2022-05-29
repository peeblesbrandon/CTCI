def stringCompression(input):
    output = []
    i = 0
    while i < len(input):
        if i == 0 or output[-2] != input[i]:
            output.append(input[i])
            output.append(1)
        else:
            if input[i] == output[-2]:
                output[-1] += 1
        i += 1
    outputStr = ''.join([str(elem) for elem in output])
    if len(outputStr) < len(input):
        return outputStr
    return input


if __name__ == '__main__':
    print(stringCompression('aabcccccaaa'))
    print(stringCompression('aabccccDDDDDDDDDDDDDDDDjalksdjfcaaa'))
    print(stringCompression('abc'))
    print(stringCompression('aabbcc'))
