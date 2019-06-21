test_cases = int(input())
for _ in range(test_cases):
    flag = 0
    size = int(input())
    arr_list = list(map(int, input().split()))
    element_to_be_searched = int(input())

    for i in range(0, len(arr_list)):
        if arr_list[i] == element_to_be_searched:
            flag = 1
            print(i)
            break

    if flag == 0:
        print(-1)