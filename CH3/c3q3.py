import unittest

class SetOfStacks:
    def __init__(self, maxSubStackHeight=10):
        self.maxSubStackHeight = maxSubStackHeight
        self.stackArr = [Stack(self.maxSubStackHeight)]
        self.heightAll = 0

    def __len__(self):
        return self.heightAll
    
    def isEmpty(self):
        if self.heightAll == 0:
            return True
        return False

    def numOfStacks(self):
        return len(self.stackArr)

    def push(self, item):
        if self.stackArr[-1].isFull(): # check curr capacitiy of last stack in array
            self.stackArr.append(Stack(self.maxSubStackHeight))
        self.stackArr[-1].push(item)
        self.heightAll += 1

    def pop(self):
        popped = self.stackArr[-1].pop()
        if self.stackArr[-1].height == 0:
            self.stackArr.pop()
        self.heightAll -= 1
        return popped
    
    def peek(self):
        return self.stackArr[-1].peek()


class Stack:
    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

    def __init__(self, max_height=10):
        self.top = None
        self.height = 0
        self.max_height = max_height

    def __len__(self):
        return self.height

    def isEmpty(self):
        if self.height == 0:
            return True
        return False
    
    def isFull(self):
        if self.height == self.max_height:
            return True
        return False

    def peek(self):
        if self.isEmpty():
            raise Exception('stack is empty')
        return self.top.value

    def push(self, value):
        if self.isEmpty():
            self.top = Stack.Node(value, None)
        else:
            self.top = Stack.Node(value, self.top)
        self.height += 1

    def pop(self):
        if self.isEmpty():
            raise Exception('stack is empty')
        popped = self.top
        self.top = self.top.next
        self.height -= 1
        return popped.value

class Test(unittest.TestCase):
    def test_basic(self):
        myStackSet = SetOfStacks(5)
        for i in range(8):
            myStackSet.push(i)
        self.assertEqual(myStackSet.numOfStacks(), 2)
    
    def test_popAndRemoveEmptySubStack(self):
        myStackSet = SetOfStacks(5)
        for i in range(16):
            myStackSet.push(i)
        self.assertEqual(myStackSet.numOfStacks(), 4)
        myStackSet.pop()
        self.assertEqual(myStackSet.numOfStacks(), 3, 'should be three stacks after removing empty substack following pop')
    
    def test_heightOfAllSubStacks(self):
        myStackSet = SetOfStacks(5)
        for i in range(21):
            myStackSet.push(i)
        self.assertEqual(len(myStackSet), 21)
        for i in range(6):
            myStackSet.pop()
        self.assertEqual(len(myStackSet), 15)

if __name__ == '__main__':
    unittest.main()
