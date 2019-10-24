n = int(input())
for _ in range(n):
    size, target = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    ans_list = []
    flag = False
    for i in arr:
        if len(str(i)) <= 1:
            continue
        if i < target:
            temp = str(i)
            for j in range(len(temp)-1):
                if abs(int(temp[j]) - int(temp[j+1])) != 1:
                    break
            else:
                flag = True
                ans_list.append(i)
    if flag:
        print(" ".join(str(k) for k in ans_list))
    else:
        print(-1)