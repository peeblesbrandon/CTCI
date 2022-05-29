class Node:
    def __init__(self, val, min_below, prev=None, next=None):
        self.val = val
        self.min_below = min_below # contains min at or below current node
        self.prev = prev 
        self.next = next

class MinStack:
    def __init__(self):
        self.stack = None
        self.top = None
        self.count = 0
    
    def __len__(self):
        return self.count

    def push(self, val):
        if self.stack is None:
            self.stack = Node(val, val)
            self.top = self.stack
            self.count += 1
        else:
            self.top.next = Node(val, min(self.top.min_below, val), self.top)
            self.top = self.top.next
            self.count += 1
    
    def pop(self):
        if self.count == 0:
            raise Exception("Stack is currently empty")
        popped = self.top
        self.top = self.top.prev
        self.count -= 1
        return popped 
    
    def min(self):
        if self.count == 0:
            raise Exception("Stack is currently empty")
        return self.top.min_below


if __name__ == "__main__":
    myStack = MinStack()
    myStack.push(5)
    print(len(myStack))
    myStack.push(7)
    myStack.push(3)
    print(myStack.min())
    myStack.pop()
    print(myStack.min())
