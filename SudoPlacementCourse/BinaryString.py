test_cases = int(input())
for _ in range(test_cases):
    size = int(input())
    arr_list = input()
    ans = 0
    count = arr_list.count("1")
    i = 0
    while i < count:
        ans += i
        i += 1
    print(ans)
    # for i in range(size):
    #     #     if arr_list[i] == '1':
    #     #         for j in range(i+1, size):
    #     #             if arr_list[j] == '1':
    #     #                 count += 1
    #     # print(count)
    # for i in range(size):
    #     if arr_list[i] == '1':
    #         count += arr_list.count("1", i+1)
    # print(count)

