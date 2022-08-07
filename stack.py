class Stack:
    def __init__(self):
        self.items = []
        print(self)
        print(self.items)
        print(type(self))
        print(type(self.items))

    def push(self, item):
        self.items.append(item)

    def pop(self, item):
        self.items.pop(item)

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


myStack = Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")
myStack.push("D")
print(myStack.peek())
