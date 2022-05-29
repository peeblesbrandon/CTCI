import unittest

class Node:
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def getSuccessor(node):
    if not node:
        return None
    if node.right:
        node = node.right
        while  node.left:
            node = node.left 
        return node
    else:
        while node.parent and node.parent.right == node:
            node = node.parent 
        return node.parent

class Test(unittest.TestCase):
    def test_successorOfRoot(self):
        inputTree = Node(5, Node(3), Node(6))
        inputTree.left.parent = inputTree
        inputTree.right.parent = inputTree
        self.assertEqual(getSuccessor(inputTree), inputTree.right)
    
    def test_successorOfLeftChild(self):
        inputTree = Node(5, Node(3), Node(6))
        inputTree.left.parent = inputTree
        inputTree.right.parent = inputTree
        self.assertEqual(getSuccessor(inputTree.left), inputTree)

    def test_successorOfRightChild(self):
        inputTree = Node(5, Node(3), Node(6))
        inputTree.left.parent = inputTree
        inputTree.right.parent = inputTree
        self.assertIsNone(getSuccessor(inputTree.right))

    def test_successorOfRightChildWithRightSubtree(self):
        inputTree = Node(5, Node(3), Node(6))
        inputTree.left.parent = inputTree
        inputTree.right.parent = inputTree
        inputTree.right.right = Node(9, Node(8), Node(10))
        inputTree.right.right.parent = inputTree.right
        inputTree.right.right.left.parent = inputTree.right.right
        inputTree.right.right.right.parent = inputTree.right.right
        self.assertEqual(getSuccessor(inputTree.right), inputTree.right.right.left)

if __name__ == '__main__':
    unittest.main()
