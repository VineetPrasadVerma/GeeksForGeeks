n = int(input())
for _ in range(n):
    size = int(input())
    arr = list(map(int, input().split()))
    for i in range(size-1):
        if arr[i+1] < arr[i]:
            print(arr[i+1], end=" ")
        else:
            print(-1, end=" ")
    print(-1)
