import unittest 

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# simple solution
def isSubtree(treeToSearch, treeToFind):
    searchArray = []
    findArray = []

    preOrder(treeToSearch, searchArray)
    preOrder(treeToFind, findArray)

    treeToSearch = ''.join(searchArray)
    treeToFind = ''.join(findArray)
     
    return treeToFind in treeToSearch

def preOrder(node, array):
    if not node:
        array.append('X')
        return
    array.append(str(node.value))
    preOrder(node.left, array)
    preOrder(node.right, array)

# recursive solution (more optimal for space)
def compareTrees(node1, node2):
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    if node1.value == node2.value:
        return compareTrees(node1.left, node2.left) \
            and compareTrees(node1.right, node2.right)
    return
    

def searchTree(treeToSearch, treeToFind):
    if treeToSearch is None:
        return False
    if treeToFind is None:
        return True # empty tree is always subtree of another tree
    if treeToSearch.value == treeToFind.value:
        # potential subtree - need to compare and validate
        if compareTrees(treeToSearch, treeToFind):
            return True
    return searchTree(treeToSearch.left, treeToFind) \
        or searchTree(treeToSearch.right, treeToFind)
    

# tests
class Test(unittest.TestCase):
    # SIMPLE SOLUTION
    def test_isSubtree_simple(self):
        treeToSearch = Node(4, Node(2, Node(1), Node(6)), Node(0, Node(1), Node(2)))
        treeToFind = Node(0, Node(1), Node(2))
        self.assertTrue(isSubtree(treeToSearch, treeToFind))
    
    def test_isNotSubtree_simple(self):
        # preorder traversal without the None placeholders would evaluate this to True
        treeToSearch = Node(4, Node(2, Node(1), Node(6)), Node(0, Node(2), None))
        treeToFind = Node(0, None, Node(2))
        self.assertFalse(isSubtree(treeToSearch, treeToFind))
    
    def test_emptySubtree_simple(self):
        treeToSearch = Node(4, Node(2, Node(1), Node(6)))
        treeToFind = None
        self.assertTrue(isSubtree(treeToSearch, treeToFind))
    
    # RECURSIVE SOLUTION
    def test_isSubtree_recursive(self):
        treeToSearch = Node(4, Node(2, Node(1), Node(6)),
                            Node(0, Node(1), Node(2)))
        treeToFind = Node(0, Node(1), Node(2))
        self.assertTrue(searchTree(treeToSearch, treeToFind))

    def test_isNotSubtree_recursive(self):
        treeToSearch = Node(4, Node(2, Node(1), Node(6)),
                            Node(0, Node(2), None))
        treeToFind = Node(0, None, Node(2))
        self.assertFalse(searchTree(treeToSearch, treeToFind))

    def test_emptySubtree_recursive(self):
        treeToSearch = Node(4, Node(2, Node(1), Node(6)))
        treeToFind = None
        self.assertTrue(searchTree(treeToSearch, treeToFind))
    
if __name__ == '__main__':
    unittest.main()
