import math
t = int(input())
for _ in range(t):
    x, y = tuple(map(int, input().split()))
    if y == 0:
        if x == 1:
            print(1)
            continue
        else:
            print(0)
            continue
    k = int(math.log(y, x))
    if x ** k == y:
        print(1)
    else:
        print(0)