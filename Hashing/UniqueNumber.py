n = int(input())
for _ in range(n):
    m, n = tuple(map(int, input().split()))
    for i in range(m, n+1):
        if sorted(str(i)) == sorted(set(str(i))):
            print(str(i), end=" ")
    print()