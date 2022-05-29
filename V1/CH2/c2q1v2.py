"""
seen = set()
for each node:
    if in set:
        delete
    else:
        add to set
    advance to next node

O(N) time
O(N) space

to use constant space, we'd require quadratic runtime

node:
    node.val
    node.next
"""

def removeDupes(head):
    if not head:
        return head
    seen = set()
    prev, curr = None, head
    while curr:
        if curr.val in seen:
            prev.next = curr.next
        else:
            seen.add(curr.val)
            prev = curr
        curr = curr.next


