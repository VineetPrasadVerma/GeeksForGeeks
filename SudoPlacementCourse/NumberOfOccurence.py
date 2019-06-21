test_cases = int(input())
for _ in range(test_cases):
    count = 0
    size, element = tuple(map(int, input().split()))
    arr_list = list(map(int, input().split()))
    for i in arr_list:
        if i == element:
            count += 1
    if count > 0:
        print(count)
    else:
        print(-1)