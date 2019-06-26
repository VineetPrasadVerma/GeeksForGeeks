import math
test_cases = int(input())
for _ in range(test_cases):
    num = int(input())
    temp = num
    counter = 0
    ans = 1
    while num != 0 and num != 1:
        num = num / 8
        counter += 1
    for i in range(0, counter):
        ans *= 8
    if ans == temp or ans == 8:
        print("Yes")
    else:
        print("No")