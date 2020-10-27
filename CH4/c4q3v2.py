from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def listOfDepths(root):
    level = 0
    lists = {}
    lists[level] = deque()
    sentinel = 'X'
    queue = deque()
    queue.append(root)
    queue.append(sentinel) # mark the end of a level
    while queue:
        node = queue.popleft()
        if node == sentinel:
            level += 1
            # add another sentinel if the queue isnt empty (to avoid looping)
            if queue:
                queue.append(sentinel)
                lists[level] = deque()
        else:
            lists[level].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return lists
            

if __name__ == "__main__":
    tree = Node(1, 
            Node(2, 
                Node(3), Node(3)
                ),
            Node(2, 
                Node(3), Node(3)
                )
            )
    print(listOfDepths(tree))
        
