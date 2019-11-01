def sublist(arr):
    lst = []
    if len(arr) == 1:
        return [arr]
    for i in range(1, len(arr)+1):
        lst.append(arr[:i])
    return lst + sublist(arr[1:])


n = int(input())
for _ in range(n):
    count = 0
    size = int(input())
    arr = list(map(int, input().split()))
    print(len(sublist(arr)))
    for lst in sublist(arr):
        if sum(lst) == 0:
            count += 1
    print(count)

