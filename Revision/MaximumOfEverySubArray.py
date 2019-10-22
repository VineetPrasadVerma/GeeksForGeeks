n = int(input())
for _ in range(n):
    size, window = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    for i in range(0, size-window+1):
        print(max(arr[i: i+window]), end=" ")
    print()
