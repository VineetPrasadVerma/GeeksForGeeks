from itertools import combinations
n = int(input())
for _ in range(n):
    sums = 0
    size = int(input())
    arr = list(map(int, input().split()))
    all_pairs = list(combinations(arr, 2))
    for pair in all_pairs:
        if abs(pair[-1] - pair[0]) > 1:
            sums += pair[-1] - pair[0]
        else:
            sums += 0
    print(sums)
