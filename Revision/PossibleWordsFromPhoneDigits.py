n = int(input())
for _ in range(n):
    size, window = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    sub_lists = []
    for i in range(0, size, window):
        sub_lists.append(arr[i: i + window])
    print(sub_lists)