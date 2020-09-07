# incomplete -- will revisit later

from collections import deque

def generateBSTarrays(root):
    if root:
        generateBSTarrays_leftright([root])

def generateBSTarrays_leftright(array):
    # use recursion and pre-order traversal to generate arrays
    if not array[-1].left and not array[-1].right:
        print(array)
    newArray = array
    if newArray[-1].left:
        newArray.append(newArray[-1].left)
        generateBSTarrays_leftright(array[-1].left)
    if newArray[-1].right:
        newArray.append(newArray[-1].right)
        generateBSTarrays_leftright(array[-1].right)
    
def generateBSTarrays_rightleft(array):
    # use recursion and pre-order traversal to generate arrays
    if not array[-1].left and not array[-1].right:
        print(array)
    newArray = array
    if newArray[-1].right:
        newArray.append(newArray[-1].right)
        generateBSTarrays_rightleft(array[-1].right)
    if newArray[-1].left:
        newArray.append(newArray[-1].left)
        generateBSTarrays_rightleft(array[-1].left)

