import unittest

def zeroMatrix(mtrx):
    if not mtrx:
        return False
    M, N = [], []
    # locate positions of 0's
    for i in range(len(mtrx)):
        for j in range(len(mtrx[i])):
            if mtrx[i][j] == 0:
                M.append(i)
                N.append(j)
    # zero out columns
    for col in M:
        for j in range(len(mtrx[col])):
            mtrx[col][j] = 0
    # zero out rows
    for row in N:
        for i in range(len(mtrx)):
            mtrx[i][row] = 0
    return mtrx 

class Test(unittest.TestCase):
    def test_3x3(self):
        input  = [[1,2,0],
                  [0,5,0],
                  [7,8,9]]
        output = [[0,0,0],
                  [0,0,0],
                  [0,8,0]]
        self.assertEqual(zeroMatrix(input), output)
    
    def test_4x4(self):
        input  = [[1,2,3,4],
                  [1,2,3,4],
                  [1,2,3,0]]
        output  = [[1,2,3,0],
                   [1,2,3,0],
                   [0,0,0,0]]
        self.assertEqual(zeroMatrix(input), output)
                         
    def test_0x0(self):
        input = None
        self.assertFalse(zeroMatrix(input))

if __name__ == '__main__':
    unittest.main()