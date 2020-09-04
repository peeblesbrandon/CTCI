class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, node):
        if self.head:
            curr = self.head 
            while curr.next:
                curr = curr.next 
            curr.next = node 
        else:
            self.head = node 

    def appendLeft(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    def __len__(self):
        if not self.head:
            return 0
        len = 0
        curr = self.head
        while curr:
            len += 1
            curr = curr.next
        return len

    def reverse(self):
        if self.head:
            curr = self.head
            prev = None
            next = None
            while curr:
                next = curr.next 
                curr.next = prev
                prev = curr 
                curr = next 
            self.head = prev 
            return prev

    
    def print(self):
        if self.head:
            curr = self.head
            while curr:
                print(curr.value)
                curr = curr.next
    
