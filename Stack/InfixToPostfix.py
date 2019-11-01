operator_stack = []
postfix = []
infix = "a+b*(c^d-e)^(f+g*h)-i"

precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}


def is_operand(char):
    if char.isalpha():
        return True
    else:
        return False


def check_precedence(char):
    if operator_stack[-1] not in precedence.keys():
        return False
    elif precedence[char] <= precedence[operator_stack[-1]]:
        return True
    else:
        return False


for i in infix:

    if is_operand(i):
        postfix.append(i)

    else:
        if i == "(":
            operator_stack.append(i)

        elif i == ")":
            while len(operator_stack) != 0 and operator_stack[-1] != "(":
                postfix.append(operator_stack[-1])
                del operator_stack[-1]
            del operator_stack[-1]

        else:
            while len(operator_stack) != 0 and check_precedence(i):
                postfix.append(operator_stack[-1])
                del operator_stack[-1]
            operator_stack.append(i)

while len(operator_stack) != 0:
    postfix.append(operator_stack[-1])
    del operator_stack[-1]

print("".join(postfix))