test_cases = int(input())
for _ in range(test_cases):
    size = int(input())
    arr = list(map(int, input().split()))
    actual_arr = [i for i in range(1, size+1)]
    a = set(actual_arr)-set(arr)
    for i in a:
        print(i)
