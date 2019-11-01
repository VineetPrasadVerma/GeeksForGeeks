n = int(input())
for _ in range(n):
    stack = []
    expression = input()
    count = 1
    for i in expression:
        if i == "(":
            stack.append(count)
            print(count, end=" ")
            count += 1
        elif i == ")":
            temp = stack.pop()
            print(temp, end=" ")
        print()
