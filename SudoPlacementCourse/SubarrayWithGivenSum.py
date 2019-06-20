test_cases = int(input())
for _ in range(test_cases):
    flag = 0
    size, sums = tuple(map(int, input().split()))
    arr_list = list(map(int, input().split()))
    temp_sum = 0
    start = 0
    end = 0
    for i in range(0, len(arr_list)):
        if temp_sum < sums:
            temp_sum += arr_list[i]
            end = i
        if temp_sum > sums:
            while sums < temp_sum:
                temp_sum -= arr_list[start]
                start += 1
        if temp_sum == sums:
            flag = 1
            print(start+1, end+1)
            break
    if flag == 0:
        print(-1)




