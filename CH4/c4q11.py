from random import random 
import unittest


class Node:
    def __init__(self, value=None, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
    
    def isLeaf(self):
        if self.left is None and self.right is None:
            return True
        return False

    def hasBothChildren(self):
        if self.left and self.right:
            return True
        return False

    def isRightChild(self):
        if self.parent.right == self:
            return True
        return False

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.nodeCount = 0
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
        self.nodeCount += 1
    
    def _insert(self, value, node):
        if value > node.value:
            if node.right is None:
                node.right = Node(value, node)
            else:
                return self._insert(value, node.right)
        elif value < node.value:
            if node.left is None:
                node.left = Node(value, node)
            else:
                return self._insert(value, node.left)
        else:
            raise Exception('value already exists in tree')

    def find(self, value):
        if not self.root:
            raise Exception('tree is empty')
        return self._find(value, self.root)
        
    def _find(self, value, node):
        if node is None:
            raise Exception('value not found in tree')
        elif value < node.value:
            return self._find(value, node.left)
        elif value > node.value:
            return self._find(value, node.right)
        else:
            return node

    def delete(self, value):
        nodeToDelete = self.find(value)
        if nodeToDelete.isLeaf():
            nodeToDelete = None
        elif nodeToDelete.hasBothChildren():
            replacement = nodeToDelete.left
            while replacement.right: # locate greatest value strictly less than nodeToDelete (rightmost child of left subtree)
                replacement = replacement.right
            nodeToDelete.value, replacement.value = replacement.value, nodeToDelete.value
            if replacement.left:
                replacement.left.parent = replacement.parent 
            replacement.parent.right = replacement.left
            replacement = None
        else:
            if nodeToDelete.left:
                nodeToDelete.left.parent = nodeToDelete.parent 
                if nodeToDelete.isRightChild():
                    nodeToDelete.parent.right = nodeToDelete.left
                else: 
                    nodeToDelete.parent.left = nodeToDelete.left 
            else:
                nodeToDelete.right.parent = nodeToDelete.parent 
                if nodeToDelete.isRightChild():
                    nodeToDelete.parent.right = nodeToDelete.right
                else:
                    nodeToDelete.parent.left = nodeToDelete.right
        self.nodeCount -= 1

    def getRandomNode_slow(self):
        nodesArray = [] 
        self._getRandomNode_slow(self.root, nodesArray)
        randomIndex = int(round(len(nodesArray) * random(), 0))
        return nodesArray[randomIndex]

    def _getRandomNode_slow(self, node, array):
        if node:
            array.append(node)
            self._getRandomNode_slow(node.left, array)
            self._getRandomNode_slow(node.right, array)
            
    
class Test(unittest.TestCase):
    def test_insert(self):
        myBST = BinarySearchTree()
        myBST.insert(5)
        myBST.insert(3)
        myBST.insert(9)
        myBST.insert(8)
        myBST.insert(7)
        myBST.insert(1)
        self.assertEqual(myBST.nodeCount, 6)
    
    def test_find(self):
        myBST = BinarySearchTree()
        myBST.insert(5)
        myBST.insert(3)
        myBST.insert(9)
        myBST.insert(8)
        myBST.insert(7)
        myBST.insert(1)
        self.assertIsInstance(myBST.find(9), Node)

    def test_delete(self):
        myBST = BinarySearchTree()
        myBST.insert(5)
        myBST.insert(3)
        myBST.insert(4)
        myBST.insert(9)
        myBST.insert(8)
        myBST.insert(7)
        myBST.insert(1)
        myBST.delete(9)
        self.assertEqual(myBST.nodeCount, 6)
        myBST.delete(3)
        self.assertEqual(myBST.nodeCount, 5)

    def test_getRandomNode_slow(self):
        myBST = BinarySearchTree()
        myBST.insert(5)
        myBST.insert(3)
        myBST.insert(4)
        myBST.insert(9)
        myBST.insert(8)
        myBST.insert(7)
        myBST.insert(1)
        self.assertIsInstance(myBST.getRandomNode_slow(), Node)


if __name__ == '__main__':
    unittest.main()
        
