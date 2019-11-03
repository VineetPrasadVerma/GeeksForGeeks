n = int(input())
for _ in range(n):
    size = int(input())
    arr = [int(i) for i in input().split()]
    ans = [-1]
    stack = []
    top = 0
    for i in range(size-2, -1, -1):

        if arr[i] < arr[i + 1]:
            ans.append(arr[i + 1])
            stack.append(arr[i + 1])
            top += 1
        else:
            if i == size - 2:
                stack = [arr[-1]]
                top += 1
            temp = top
            while arr[i] > stack[temp-1] and temp != 0:
                temp -= 1
            if temp == 0:
                ans.append(-1)
            else:
                ans.append(stack[temp-1])

    print(" ".join(str(i) for i in ans[::-1]))