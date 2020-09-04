from LinkedList import Node, LinkedList
import unittest

def hasIntersect(L1, L2):
    if not L1 or not L2:
        return False
    curr1 = L1.head
    curr2 = L2.head
    len1 = 1
    len2 = 1
    while curr1.next:
        len1 += 1
        curr1 = curr1.next
    while curr2.next:
        len2 += 1
        curr2 = curr2.next
    if curr1 != curr2:
         return False
    if len1 >= len2:
        curr1 = L1.head
        curr2 = L2.head
        for i in range(len1 - len2):    
            curr1 = curr1.next
        while curr1 and curr2:
            if curr1 == curr2:
                return curr1
            curr1 = curr1.next
            curr2 = curr2.next
    else:
        curr1 = L1.head
        curr2 = L2.head
        for i in range(len2 - len1):
            curr2 = curr2.next
        while curr1 and curr2:
            if curr1 == curr2:
                return curr1
            curr1 = curr1.next
            curr2 = curr2.next

class Test(unittest.TestCase):
    def test_basicIntersect(self):
        # build list 1
        input1 = LinkedList()
        input1.append(Node(1))
        input1.append(Node(3))
        # build list 2
        input2 = LinkedList()
        input2.append(Node(4))
        input2.append(Node(7))
        # build list for prev 2 to share
        sharedList = LinkedList()
        sharedList.append(Node(2))
        sharedList.append(Node(8))
        # append head of sharedList to both list 1 and 2
        input1.append(sharedList.head)
        input2.append(sharedList.head)
        # test
        self.assertEqual(hasIntersect(input1, input2), sharedList.head)
    
    def test_basicNoIntersect(self):
        # build list 1
        input1 = LinkedList()
        input1.append(Node(1))
        input1.append(Node(3))
        input1.append(Node(2))
        # build list 2
        input2 = LinkedList()
        input2.append(Node(4))
        input2.append(Node(7))
        input2.append(Node(2))
        # test
        self.assertFalse(hasIntersect(input1, input2))

    def test_unequalLength(self):
        # build list 1
        input1 = LinkedList()
        input1.append(Node(1))
        input1.append(Node(3))
        input1.append(Node(7))
        input1.append(Node(9))
        input1.append(Node(2))
        # build list 2
        input2 = LinkedList()
        input2.append(Node(3))
        input2.append(Node(0))
        # build list for prev 2 to share
        sharedList = LinkedList()
        sharedList.append(Node(7))
        sharedList.append(Node(1))
        sharedList.append(Node(8))
        # append head of sharedList to both list 1 and 2
        input1.append(sharedList.head)
        input2.append(sharedList.head)
        # test
        self.assertEqual(hasIntersect(input1, input2), sharedList.head)

if __name__ == '__main__':
    unittest.main()
