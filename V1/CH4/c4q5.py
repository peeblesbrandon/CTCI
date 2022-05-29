import unittest

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left 
        self.right = right
    
def validateBST(rootNode):
    return checkBST(rootNode)

def checkBST(node, min = float('-inf'), max = float('inf')):
    if not node:
        return True
    if (node.value > min and
        node.value < max and 
        checkBST(node.left, min, node.value) and 
        checkBST(node.right, node.value, max)):
        return True
    else:
        return False

class Test(unittest.TestCase):
    def test_simpleValidBST(self):
        inputTree = Node(5, Node(3), Node(8))
        self.assertTrue(validateBST(inputTree))
    
    def test_simpleInvalidBST(self):
        inputTree = Node(5, Node(9), Node(8))
        self.assertFalse(validateBST(inputTree))

if __name__ == '__main__':
    unittest.main()