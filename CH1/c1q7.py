import pprint
pp = pprint.PrettyPrinter(indent=4)

def rotateMatrix(image): # list of lists of ints
    N = len(image)
    layers = N // 2
    for offset in range(layers):
        print(f"offset is {offset}")
        for i in range(offset, N - offset - 1):
            print(f"i is {i} and range is {offset} to {N - offset - 1}")
            # rotate by swapping values
            temp = image[offset][i + offset] # save top as temp

            image[offset][i + offset] = (
                image[N - 1 - offset - i][offset]) # left to top

            image[N - 1 - offset - i][offset] = (
                image[N - 1 - offset][N - 1 - offset - i]) # bottom to left

            image[N - 1 - offset][N - 1 - offset - i] = (
                image[i + offset][N - 1 - offset]) # right to bottom

            image[i + offset][N - 1 - offset] = temp # temp to right
    return image

if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4]
    ]
    result = [
        [1, 1, 1, 1],
        [2, 2, 2, 2],
        [3, 3, 3, 3],
        [4, 4, 4, 4]
    ]
    # print(matrix)
    # print(rotateMatrix(matrix))
    matrix = [
        [1, 2, 3, 4, 5, 6, 7],
        [1, 2, 3, 4, 5, 6, 7],
        [1, 2, 3, 4, 5, 6, 7],
        [1, 2, 3, 4, 5, 6, 7],
        [1, 2, 3, 4, 5, 6, 7],
        [1, 2, 3, 4, 5, 6, 7],
        [1, 2, 3, 4, 5, 6, 7]
    ]
    result = [
        [1, 1, 1, 1],
        [2, 2, 2, 2],
        [3, 3, 3, 3],
        [4, 4, 4, 4]
    ]
    pp.pprint(matrix)
    print("\n")
    pp.pprint(rotateMatrix(matrix))

