n = int(input())
for _ in range(n):
    size = int(input())
    arr = list(map(int, input().split()))
    sum1 = 0
    sum2 = 0
    for i in range(1, size+1):
        sum1 += arr[i-1]
        for j in range(size-1, i-1, -1):
            sum2 += arr[j]
        if sum1 == sum2:
            print(i+1)
            break
    else:
        print(-1)
