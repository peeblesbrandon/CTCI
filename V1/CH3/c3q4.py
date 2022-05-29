import unittest
from Stack import Stack

class MyQueue:
    def __init__(self):
        self.main = Stack()
        self.temp = Stack()
    
    def __len__(self):
        return max(len(self.main), len(self.temp))
    
    def _transferStacks(self):
        if not self.main.isEmpty():
            while not self.main.isEmpty():
                self.temp.push(self.main.pop())
        elif not self.temp.isEmpty():
            while not self.temp.isEmpty():
                self.main.push(self.temp.pop())
        
    def pop(self):
        if self.main.isEmpty() and self.temp.isEmpty():
            raise Exception('Queue empty')
        elif self.main.isEmpty():
            self._transferStacks()
        return self.main.pop()
    
    def push(self, item):
        if self.main.isEmpty() and not self.temp.isEmpty():
            self._transferStacks()
        self.main.push(item)

    def popleft(self):
        if self.main.isEmpty() and self.temp.isEmpty():
            raise Exception('Queue empty')
        elif not self.main.isEmpty() and self.temp.isEmpty():
            self._transferStacks()
        return self.temp.pop()
    
    def pushleft(self, item):
        if not self.main.isEmpty() and self.temp.isEmpty():
            self._transferStacks()
        self.temp.push(item)

class Test(unittest.TestCase):
    def test_basic(self):
        myQueue = MyQueue()
        myQueue.push(1)
        myQueue.push(2)
        myQueue.push(3)
        myQueue.push(4)
        self.assertEqual(myQueue.pop(), 4)
        self.assertEqual(myQueue.popleft(), 1)

if __name__ == '__main__':
    unittest.main()