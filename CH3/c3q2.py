import unittest

class MinStack:
    class Node:
        def __init__(self, value=None, next=None, localMin=None):
            self.value = value
            self.next = next
            self.localMin = localMin
        
    def __init__(self):
        self.top = None
        self.height = 0

    def __len__(self):
        return self.height

    def isEmpty(self):
        if self.height == 0:
            return True
        return False
    
    def peek(self):
        if self.isEmpty():
            raise Exception('stack is empty')
        return self.top.value
    
    def push(self, value):
        if self.isEmpty():
            self.top = MinStack.Node(value, None, value)
        else:
            localMin = min(value, self.top.localMin)
            self.top = MinStack.Node(value, self.top, localMin)
        self.height += 1

    def pop(self):
        if self.isEmpty():
            raise Exception('stack is empty')
        popped = self.top
        self.top = self.top.next
        self.height -= 1
        return popped.value
    
    def minValue(self):
        if self.isEmpty():
            raise Exception('stack is empty')
        return self.top.localMin

class Test(unittest.TestCase):
    def test_basicGetMin(self):
        myStack = MinStack()
        myStack.push(4)
        myStack.push(3)
        myStack.push(5)
        self.assertEqual(myStack.minValue(), 3)

    def test_minAfterPop(self):
        myStack = MinStack()
        myStack.push(4)
        myStack.push(3)
        myStack.push(5)
        myStack.push(2)
        self.assertEqual(myStack.minValue(), 2)
        myStack.pop()
        self.assertEqual(myStack.minValue(), 3, 'min after popping top element should be 3')

if __name__ == '__main__':
    unittest.main()
