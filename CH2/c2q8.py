from LinkedList import Node, LinkedList
import unittest

def hasLoop(list):
    slow = list.head
    fast = list.head
    while slow and fast:
        # iterate pointers and make sure we didnt reach end of the list (e.g. no loop)
        if slow:
            slow = slow.next
        else:
            return False
        if fast.next:
            fast = fast.next.next
        else:
            return False
        if slow == fast:    # check for collision
            break 
        
    slow = list.head    # reset slow pointer and iterate both slow and fast at same pace to find intersect
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow # intersection found

class Test(unittest.TestCase):
    def test_loopExists(self):
        loop = LinkedList()
        loop.append(Node(4))
        loop.append(Node(5))
        loop.append(Node(6))
        loop.append(Node(7))
        loop.append(Node(8))
        loop.append(Node(9))
        loop.append(loop.head)
        input = LinkedList()
        input.append(Node(1))
        input.append(Node(2))
        input.append(Node(3))
        input.append(loop.head)
        output = loop.head
        self.assertEqual(hasLoop(input), output)
    
    def test_noLoopExists(self):
        input = LinkedList()
        input.append(Node(1))
        input.append(Node(2))
        input.append(Node(3))
        input.append(Node(4))
        input.append(Node(5))
        input.append(Node(6))
        input.append(Node(7))
        input.append(Node(8))
        input.append(Node(9))
        self.assertFalse(hasLoop(input))

if __name__ == '__main__':
    unittest.main()
