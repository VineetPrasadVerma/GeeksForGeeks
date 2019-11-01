n = int(input())
given_set = {1, 2, 3}
for _ in range(n):
    final_list = []
    size = int(input())
    arr = input().split()
    for elm in arr:
        flag = False
        for i in elm:
            if int(i) in given_set:
                flag = True
            else:
                flag = False
                break
        if flag:
            final_list.append(int(elm))
    if len(final_list) == 0:
        print(-1)
    else:
        print(" ".join(str(i) for i in sorted(final_list)))


