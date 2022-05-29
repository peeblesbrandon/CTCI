def rotateMatrix(matrix):
    if not matrix:
        return
    N = len(matrix)
    for l in range(0, N // 2):
        for i in range(l, N - 1 - l):
            # TL, TR, BR, BL = BL, TL, TR, BR
            (
                matrix[l][i],
                matrix[i][N - 1 - l],
                matrix[N - 1 - l][N - 1 - i],
                matrix[N - 1 - i][l]
            ) = (
                matrix[N - 1 - i][l],
                matrix[l][i],
                matrix[i][N - 1 - l],
                matrix[N - 1 - l][N - 1 - i]
            )
    return matrix

if __name__ == '__main__':
    test = [[1,2,3],[4,5,6],[7,8,9]]
    print(rotateMatrix(test))
