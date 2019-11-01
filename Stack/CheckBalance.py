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


def check_balance(expression):
    stack = Stack()
    if stack.is_empty():
        if expression[0] == '}' or expression[0] == ']' or expression[0] == ')':
            return "not balanced"
    stack.push(expression[0])
    for i in expression[1:]:
        if i == "[":
            if stack.peek() == "]":
                stack.pop()
            else:
                stack.push(i)

        elif i == "{":
            if stack.peek() == "}":
                stack.pop()
            else:
                stack.push(i)

        elif i == "(":
            if stack.peek() == ")":
                stack.pop()
            else:
                stack.push(i)

        elif i == "]":
            if stack.peek() == "[":
                stack.pop()
            else:
                stack.push(i)

        elif i == "}":
            if stack.peek() == "{":
                stack.pop()
            else:
                stack.push(i)

        elif i == ")":
            if stack.peek() == "(":
                stack.pop()
            else:
                stack.push(i)
    else:
        if stack.is_empty():
            return "balanced"
        else:
            return "not balanced"


n = int(input())
for _ in range(n):
    expression = input()
    print(check_balance(expression))