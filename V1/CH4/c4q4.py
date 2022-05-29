import unittest

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value 
        self.left = left 
        self.right = right

def isBalanced(rootNode):
    if _isBalanced(rootNode) == False:
        return False
    else:
        return True

def _isBalanced(rootNode):
    if not rootNode:
        return -1
    else:
        leftHeight = _isBalanced(rootNode.left)
        rightHeight = _isBalanced(rootNode.right)
        if leftHeight is False or rightHeight is False:
            return False
        if abs(leftHeight - rightHeight) > 1:
            return False
        else:
            return max(leftHeight, rightHeight) + 1

class Test(unittest.TestCase):
    def test_isBalanced(self):
        inputNode = Node(4, 
                            Node(2, Node(1), Node(3)), 
                            Node(7)
                        ) 
        self.assertTrue(isBalanced(inputNode))

    def test_isNotBalanced(self):
        inputNode = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(6, Node(5)))) 
        self.assertFalse(isBalanced(inputNode))

if __name__ == '__main__':
    unittest.main()
