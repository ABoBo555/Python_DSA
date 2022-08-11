class Test:
    def __init__(self):
        self.items = []
        print(self)
        print(self.items)
        print(type(self))
        print(type(self.items))

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        # print(self)
        # print(self.items)
        return False, True
        # in python it can return more than 1 val but only true is accepted see @peek() if clauses
        # even you try return True, False

    def peek(self):
        print(self)
        print(self.items)
        if self.is_empty():  # accpeted only return value of 'True' not 'False'
            return self.items[-1]
        if not self.is_empty():
            return self.items[-2]


myStack = Test()
myStack.push("A")
myStack.push("B")
myStack.push("C")
myStack.push("D")
print(myStack.peek())
