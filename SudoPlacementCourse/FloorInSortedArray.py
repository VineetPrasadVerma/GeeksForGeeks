test_cases = int(input())
for _ in range(test_cases):
    size, element = tuple(map(int, input().split()))
    arr_list = list(map(int, input().split()))
    for i in range(size):
        if arr_list[i] > element:
            if i == 0:
                print(-1)
                break
            else:
                print(i-1)
                break
    else:
        print(i)


