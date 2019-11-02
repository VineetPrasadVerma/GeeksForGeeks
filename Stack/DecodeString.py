n = int(input())
for _ in range(n):
    s = input()
    stack = []
    result = ""
    for i in range(len(s)):
        if s[i] == "]" and i != len(s) - 1:
            temp1 = ""
            while stack[-1] != '[':
                temp1 += stack.pop()
            stack.pop()
            result = temp1[::-1]
            mul = ""
            temp = stack.pop()
            while temp.isdigit():
                mul += temp
                if len(stack) != 0:
                    temp = stack[-1]
                else:
                    break
            mul = "".join(mul[::-1])
            result = int(mul) * result
            final = result
            for m in final:
                stack.append(m)
        elif s[i] == "[" or s[i].isdigit() or s[i].isalpha():
            stack.append(s[i])
        elif s[i] == "]" and i == len(s) - 1:
            temp = ""
            while stack[-1] != "[":
                temp += stack.pop()
            stack.pop()
            final = temp[::-1]
            mul = ""
            temp = stack.pop()
            while temp.isdigit():
                mul += temp
                if len(stack) != 0:
                    temp = stack[-1]
                else:
                    break
            mul = "".join(mul[::-1])
            final = int(mul) * final
            for n in final:
                stack.append(n)
            break

    print("".join(i for i in stack))
