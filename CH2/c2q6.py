from LinkedList import LinkedList, Node
from collections import deque 
import unittest

def isPalindrome(list):
    if not list.head:
        return False
    curr = list.head
    stack = deque()
    while curr:
        stack.append(curr.value)
        curr = curr.next
    curr = list.head
    while curr:
        if curr.value != stack.pop():
            return False
        curr = curr.next
    return True

class Test(unittest.TestCase):
    def test_simplePalindrome(self):
        input = LinkedList()
        input.append(Node(1))
        input.append(Node(2))
        input.append(Node(1))
        self.assertTrue(isPalindrome(input))

    def test_simpleNotPalindrome(self):
        input = LinkedList()
        input.append(Node(5))
        input.append(Node(3))
        input.append(Node(9))
        self.assertFalse(isPalindrome(input))

    def test_longPalindrome(self):
        input = LinkedList()
        input.append(Node(5))
        input.append(Node(3))
        input.append(Node(5))
        input.append(Node(3))
        input.append(Node(0))
        input.append(Node(9))
        input.append(Node(3))
        input.append(Node(5))
        input.append(Node(3))
        input.append(Node(5))
        self.assertFalse(isPalindrome(input))
    
if __name__ == '__main__':
    unittest.main()
