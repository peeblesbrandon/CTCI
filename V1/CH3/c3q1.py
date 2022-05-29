import unittest

class TriStack:
    def __init__(self, stacksize):
        self.numstacks = 3
        self.stacksize = stacksize
        self.array = [None] * (self.numstacks * self.stacksize)
        self.heights = [0] * self.numstacks

    def push(self, item, stacknum):
        if self.heights[stacknum] == self.stacksize:
            raise Exception(f'stack {stacknum} is full')
        offset = (stacknum * self.stacksize) + (self.heights[stacknum])
        self.array[offset] = item
        self.heights[stacknum] += 1

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            raise Exception(f'stack {stacknum} is empty')
        offset = (stacknum * self.stacksize) + (self.heights[stacknum] - 1)
        popped = self.array[offset]
        self.array[offset] = None
        self.heights[stacknum] -= 1
        return popped
    
    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            raise Exception(f'stack {stacknum} is empty')
        offset = (stacknum * self.stacksize) + (self.heights[stacknum] - 1)
        return self.array[offset]
        
    def isEmpty(self, stacknum):
        if self.heights[stacknum] == 0:
            return True
        return False 

class Test(unittest.TestCase):
    def test_basic(self):
        tristack = TriStack(10)
        tristack.push(3, 2)
        tristack.push(8, 0)
        tristack.push(2, 2)
        tristack.push(1, 1)
        self.assertEqual(tristack.pop(1), 1)
        self.assertTrue(tristack.isEmpty(1))
        self.assertEqual(tristack.peek(0), 8)
    
    def test_fullStack(self):
        tristack = TriStack(3)
        for i in range(3):
            tristack.push(i, 0)
        self.assertRaises(Exception, tristack.push, 3, 0)

if __name__ == '__main__':
    unittest.main()
