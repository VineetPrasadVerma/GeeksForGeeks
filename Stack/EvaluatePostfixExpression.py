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



def is_digit(elm):
    if elm.isdigit():
        return True
    else:
        return False


n = int(input())
for _ in range(n):
    stack = Stack()
    expression = input()
    for i in expression:
        if is_digit(i):
            stack.push(i)
        else:
            temp1 = int(stack.pop())
            temp2 = int(stack.pop())
            if i == "*":
                stack.push(temp1 * temp2)
            elif i == "/":
                stack.push(int((temp2 / temp1)))
            elif i == "+":
                stack.push(temp1 + temp2)
            else:
                stack.push(temp2 - temp1)
    print(stack.peek())