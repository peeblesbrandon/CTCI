"""
class Node:
    def __init__(val=None, next=None):
        self.val = val
        self.next = next

solution:
    catch bad calls/edge cases
    # first pass
    get length of list ( get next node while curr node is not None)
    # second pass
    go to length - k ( get next Node while count is not length - k)
    return node or value 

"""

def removeKthToLast(head, k: int):
    p1 = head
    p2 = head

    # move p1 k nodes into list
    for i in range(k):
        if p1 is None: return None # out of bounds error, bad k value
        p1 = p1.next
    
    # now move p1 and p2 at same place, once p1 hits end (None) return p2
    while p1:
        p1 = p1.next
        p2 = p2.next
    
    return p2
