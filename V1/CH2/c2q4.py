from LinkedList import Node
import unittest

def partition(node, partitionVal):
    head = node 
    tail = node
    node = node.next  
    while node:
        if node.value < partitionVal:
            newHead = Node(node.value, head)
            head = newHead
        else:
            tail.next = Node(node.value)
            tail = tail.next
        node = node.next
    return head

class Test(unittest.TestCase):
    def test_basic(self):
        input = Node(5,Node(3,Node(2)))
        self.assertEqual(partition(input, 5).value, 2)
        self.assertEqual(partition(input, 5).next.value, 3)
        self.assertEqual(partition(input, 5).next.next.value, 5)

if __name__ == '__main__':
    unittest.main()
