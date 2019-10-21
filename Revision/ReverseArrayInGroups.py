n = int(input())
for _ in range(n):
    size, group = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    ans_list = []
    for i in range(0, size, group):
        ans_list.append(arr[i: i+group][::-1])
    for j in ans_list:
        for k in j:
            print(k, end=" ")
    print()
