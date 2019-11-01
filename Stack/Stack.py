class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, elm):
        self.stack.append(elm)

    def pop(self):
        if self.is_empty():
            return -1
        else:
            return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return -1 # return minus infinite
        return self.stack[-1]


stack = Stack()
stack.push(3)
stack.push(5)
stack.push(4)

print(stack.pop())
print(stack.peek())
print(stack.peek())
stack.push(10)
print(stack.peek())

