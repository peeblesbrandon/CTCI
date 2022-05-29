from collections import deque

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left 
        self.right = right 
    
# recursive solution using pre-order traversal
def getListsAtDepthsRecur(rootNode):
    lists = []
    _getListsAtDetpthsRecur(rootNode, lists, 0)
    return lists

def _getListsAtDetpthsRecur(root, lists, level):
    if not root:
        return 
    if len(lists) == level:
        list = deque()
        lists.add(list)
    else:
        list = lists[level]
    list.add(root)
    _getListsAtDetpthsRecur(root.left, lists, level + 1)
    _getListsAtDetpthsRecur(root.right, lists, level + 1)

# iterative solution using breadth first search
def getListsAtDepthsIter(rootNode):
    if rootNode:
        listsArray = []
        current = deque()
        current.append(rootNode)
        while current:
            listsArray.append(current)
            parents = current 
            current = deque()
            for parent in parents:
                if parent.left:
                    current.append(parent.left)
                if parent.right:
                    current.append(parent.right)
        return listsArray
