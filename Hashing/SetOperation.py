test_cases = int(input())
for _ in range(test_cases):
    n, m = tuple(map(int, input().split()))
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))
    operation = int(input())
    if operation == 1:
        ans = set_a & set_b
    elif operation == 2:
        ans = set_a | set_b
    elif operation == 3:
        ans = set_a ^ set_b
    elif operation == 4:
        ans = set_a - set_b
    else:
        ans = set_b - set_a

    temp = sorted(ans)
    print("{", end="")
    if len(temp) != 0:
        for i in range(len(temp)):
            if i == len(temp)-1:
                print(temp[i], end="")
            else:
                print(temp[i], end=", ")
    print("}")



