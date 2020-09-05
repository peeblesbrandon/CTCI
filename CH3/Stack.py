class Stack:
    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.top = None
        self.height = 0

    def __len__(self):
        return self.height

    def isEmpty(self):
        if self.height == 0:
            return True
        return False

    def peek(self):
        if self.isEmpty():
            raise Exception('stack is empty')
        return self.top.value

    def push(self, value):
        if self.isEmpty():
            self.top = Stack.Node(value, None)
        else:
            self.top = Stack.Node(value, self.top)
        self.height += 1

    def pop(self):
        if self.isEmpty():
            raise Exception('stack is empty')
        popped = self.top
        self.top = self.top.next
        self.height -= 1
        return popped.value
