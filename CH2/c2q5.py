import unittest
from LinkedList import LinkedList, Node

def sumLists(L1, L2):
    if not L1 and not L2: 
        return False
    if L1: 
        curr1 = L1.head
    if L2: 
        curr2 = L2.head
    output = LinkedList()
    carry = 0

    while curr1 or curr2:
        if not output.head:
            output.head = Node(0)
            curr3 = output.head 
        else:
            curr3.next = Node(0)
            curr3 = curr3.next 
        if curr1:
            curr3.value += curr1.value
        if curr2:
            curr3.value += curr2.value
        curr3.value += carry
        carry = 0
        if curr3.value > 9:
            curr3.value = curr3.value % 10
            carry = 1
        if curr1:
            curr1 = curr1.next
        if curr2:
            curr2 = curr2.next
    
    return output

class Test(unittest.TestCase):
    def test_basic(self):
        input1 = LinkedList() # 3 -> 2 -> 1, aka 123
        input1.append(Node(3))
        input1.append(Node(2))
        input1.append(Node(1))
        input2 = LinkedList() # 4 -> 3 -> 2, aka 234
        input2.append(Node(4))
        input2.append(Node(3))
        input2.append(Node(2))
        output = LinkedList() # 7 -> 5 -> 3, aka 357
        output.append(Node(7))
        output.append(Node(5))
        output.append(Node(3))
        # tests
        self.assertEqual(sumLists(input1, input2).head.value, output.head.value)
        self.assertEqual(sumLists(input1, input2).head.next.value,
                         output.head.next.value)
        self.assertEqual(sumLists(input1, input2).head.next.next.value,
                         output.head.next.next.value)

    def test_carry(self):
        input1 = LinkedList()  # 9 -> 2 -> 1, aka 129
        input1.append(Node(9))
        input1.append(Node(2))
        input1.append(Node(1))
        input2 = LinkedList()  # 4 -> 3 -> 2, aka 234
        input2.append(Node(4))
        input2.append(Node(3))
        input2.append(Node(2))
        output = LinkedList()  # 3 -> 6 -> 3, aka 363
        output.append(Node(3))
        output.append(Node(6))
        output.append(Node(3))
        # tests
        self.assertEqual(sumLists(input1, input2).head.value,
                         output.head.value)
        self.assertEqual(sumLists(input1, input2).head.next.value,
                         output.head.next.value)
        self.assertEqual(sumLists(input1, input2).head.next.next.value,
                         output.head.next.next.value)
    
    def test_diffListLengths(self):
        input1 = LinkedList()  # 9 -> 2 -> 1, aka 129
        input1.append(Node(9))
        input1.append(Node(2))
        input1.append(Node(1))
        input2 = LinkedList()  # 4 -> 3 -> 2 -> 4 -> 1, aka 14,234
        input2.append(Node(4))
        input2.append(Node(3))
        input2.append(Node(2))
        input2.append(Node(4))
        input2.append(Node(1))
        output = LinkedList()  # 3 -> 6 -> 3 -> 4 -> 1, aka 14,363
        output.append(Node(3))
        output.append(Node(6))
        output.append(Node(3))
        output.append(Node(4))
        output.append(Node(1))
        # tests
        self.assertEqual(sumLists(input1, input2).head.value,
                         output.head.value)
        self.assertEqual(sumLists(input1, input2).head.next.value,
                         output.head.next.value)
        self.assertEqual(sumLists(input1, input2).head.next.next.value,
                         output.head.next.next.value)
        self.assertEqual(sumLists(input1, input2).head.next.next.next.value,
                         output.head.next.next.next.value)
        self.assertEqual(sumLists(input1, input2).head.next.next.next.next.value,
                         output.head.next.next.next.next.value)
         
if __name__ == '__main__':
    unittest.main()
