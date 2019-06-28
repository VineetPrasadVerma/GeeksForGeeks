t = int(input())
for _ in range(t):
    num = int(input())
    temp = num
    count = 0
    while num != 0 and num != 1:
        num = num // 2
        count += 1
    cal_num = 0
    for i in range(0, count+1):
        cal_num = 2**i
    if cal_num == temp:
        print("YES")
    else:
        print("NO")