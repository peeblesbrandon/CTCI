class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkBalanced(node):
    if isBalancedSubtree(node) is not False:
        return True
    return False

def isBalancedSubtree(node):
    if node is None:
        return 0
    leftHeight = isBalancedSubtree(node.left) + 1
    rightHeight = isBalancedSubtree(node.right) + 1
    if leftHeight is False or rightHeight is False:
        return False
    if abs(leftHeight - rightHeight) > 1:
        return False
    return max(leftHeight, rightHeight)
    
    
if __name__ == "__main__":
    # balanced
    tree = Node(1, Node(2, Node(3), Node(4)), Node(3))
    print(checkBalanced(tree))
    # not balanced
    tree = Node(1, Node(2, Node(3), Node(4, Node(5))), Node(3))
    print(checkBalanced(tree))
