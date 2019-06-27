import itertools
test_cases = int(input())
for _ in range(test_cases):
    count = 0
    size = int(input())
    arr = [int(i) for i in input().split()]
    combinations = itertools.product(arr, repeat=2)
    for f in combinations:
        binary_num_first = format(f[0] if f[0] >= 0 else (1 << 32) + f[0], '032b')
        binary_num_second = format(f[-1] if f[-1] >= 0 else (1 << 32) + f[-1], '032b')
        for i in range(0, 32):
            if binary_num_first[i] != binary_num_second[i]:
                count += 1
    print(count%10**9+7)
