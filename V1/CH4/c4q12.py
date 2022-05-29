import unittest 

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# brute force solution - check every path down from every node 
def countPathsWithSum(root, targetSum):
    if not root:
        return 0
    pathsFromRoot = countPathsWithSumFromNode(root, targetSum, 0)
    pathsFromRight = countPathsWithSum(root.right, targetSum)
    pathsFromLeft = countPathsWithSum(root.left, targetSum)
    return pathsFromRoot + pathsFromRight + pathsFromLeft

def countPathsWithSumFromNode(node, targetSum, currentSum):
    if node is None:
        return 0     
    currentSum += node.value 
     
    totalPaths = 0
    if currentSum == targetSum:
        totalPaths += 1

    totalPaths += countPathsWithSumFromNode(node.left, targetSum, currentSum)
    totalPaths += countPathsWithSumFromNode(node.right, targetSum, currentSum)
    return totalPaths 

class Test(unittest.TestCase):
    def test_basic(self):
        input = Node(4, Node(2), Node(-2, Node(4)))
        self.assertEqual(countPathsWithSum(input, 6), 2)

if __name__ == '__main__':
    unittest.main()
