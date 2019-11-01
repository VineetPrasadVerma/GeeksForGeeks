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

    def get_stack(self):
        temp = ""
        for i in self.stack:
            temp += i
        return temp


stack = Stack()
n = int(input())
for _ in range(n):
    num = input()
    for i in num:
        if stack.peek() != i:
            stack.push(i)

    print(stack.get_stack())
    print()
