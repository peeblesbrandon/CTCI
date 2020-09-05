from Stack import Stack
import unittest

def sortStack(stack):
    if stack.isEmpty() or not stack:
        raise TypeError
    tempStack = Stack()
    while not stack.isEmpty():
        tmp = stack.pop()
        while not tempStack.isEmpty() and tmp < tempStack.peek():
            stack.push(tempStack.pop())
        tempStack.push(tmp)
    while not tempStack.isEmpty():
        stack.push(tempStack.pop())

class Test(unittest.TestCase):
    def test_sortFourDiff(self):
        input = Stack()
        input.push(3)
        input.push(5)
        input.push(0)
        input.push(6)
        sortStack(input)
        self.assertEqual(input.pop(), 0)
        self.assertEqual(input.pop(), 3)
        self.assertEqual(input.pop(), 5)
        self.assertEqual(input.pop(), 6)

    def test_sortFourSame(self):
        input = Stack()
        input.push(3)
        input.push(3)
        input.push(3)
        input.push(3)
        sortStack(input)
        self.assertEqual(input.pop(), 3)
        self.assertEqual(input.pop(), 3)
        self.assertEqual(input.pop(), 3)
        self.assertEqual(input.pop(), 3)

    def test_sortFiveWithDupes(self):
        input = Stack()
        input.push(3)
        input.push(3)
        input.push(0)
        input.push(9)
        input.push(7)
        sortStack(input)
        self.assertEqual(input.pop(), 0)
        self.assertEqual(input.pop(), 3)
        self.assertEqual(input.pop(), 3)
        self.assertEqual(input.pop(), 7)
        self.assertEqual(input.pop(), 9)

if __name__ == '__main__':
    unittest.main()
