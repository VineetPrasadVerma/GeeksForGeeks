test_cases = int(input())
for _ in range(test_cases):
    flag = 0
    size_of_array = int(input())
    arr_list = list(map(int, input().split()))
    total_sum = sum(arr_list)
    left_sub_list = []
    right_sub_list = []
    temp = 0
    # for i in range(len(arr_list)):
    #     left_sub_list = arr_list[:i]
    #     right_sub_list = arr_list[i+1:]
    #     if sum(left_sub_list) == sum(right_sub_list):
    #         flag = 1
    #         print(i+1)
    #         break
    # if flag == 0:
    #     print(-1)
    for i in range(0, size_of_array):
        if temp == total_sum - temp - arr_list[i]:
            flag = 1
            print(i+1)
            break
        temp += arr_list[i]
    if flag == 0:
        print(-1)