n = int(input())
for _ in range(n):
    m, n = tuple(map(int, input().split()))
    arr1 = sorted(set(map(int, input().split())))
    arr2 = sorted(set(map(int, input().split())))
    for i in arr2:
        if i not in arr1:
            print("No")
            break
    else:
        print("Yes")
