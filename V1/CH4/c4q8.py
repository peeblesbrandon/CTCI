import unittest

class Node:
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right

def getFirstCommonAncestor(root, node1, node2):
    result = getFirstCommonAncestor_helper(root, node1, node2)
    if isinstance(result, Node):
        return result
    elif result == 0:
        raise Exception('node1 and node2 not found in tree')
    elif result == 1:
        raise Exception('node2 not found in tree')
    elif result == 2:
        raise Exception('node1 not found in tree')

def getFirstCommonAncestor_helper(currNode, node1, node2):
    if currNode == None:
        return 0
    elif currNode == node1:
        return 1
    elif currNode == node2:
        return 2
    leftReturn = getFirstCommonAncestor_helper(currNode.left, node1, node2)
    if isinstance(leftReturn, Node): # if the function found the answer, bubble up
        return leftReturn 
    rightReturn = getFirstCommonAncestor_helper(currNode.right, node1, node2)
    if isinstance(rightReturn, Node):
        return rightReturn
    sumReturn = leftReturn + rightReturn
    if sumReturn == 3:
        return currNode
    else:
        return sumReturn


class Test(unittest.TestCase):
    def test_basic(self):
        input = Node(2, Node(4), Node(3))
        node1 = Node(8)
        node2 = Node(9)
        answer = input.left
        input.left.left = node1
        input.left.right = node2
        self.assertEqual(getFirstCommonAncestor(input, node1, node2), answer)
    
    def test_rootIsFCA(self):
        input = Node(2, Node(4), Node(3))
        node1 = Node(8)
        node2 = Node(9)
        answer = input
        input.left.left = node1
        input.right.right = node2
        self.assertEqual(getFirstCommonAncestor(input, node1, node2), answer)

if __name__ == '__main__':
    unittest.main() 


# time complexity: O(n)
# space complexity: O(log n)