for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    j = n - 1
    i = 0
    count = 0
    while i < j:
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        elif arr[i] < arr[j]:
            arr[i + 1] = arr[i] + arr[i+1]
            i += 1
            count += 1
        else:
            arr[j - 1] = arr[j] + arr[j - 1]
            j -= 1
            count += 1

    print(count)
