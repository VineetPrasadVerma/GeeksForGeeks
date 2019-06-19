test_cases = int(input())
for _ in range(test_cases):
    flag = 0
    temp_array = []
    size_of_array = int(input())
    int_list_of_digits = list(map(int, input().split()))
    for i in range(size_of_array):
        for k in range(i+1, size_of_array):
            temp_array.append(int_list_of_digits[i])
            temp_array.append(int_list_of_digits[k])
            left_array = list(set(int_list_of_digits) - set(temp_array))
            for item in left_array:
                if item*item == temp_array[0]*temp_array[0] + temp_array[-1]*temp_array[-1]:
                    flag = 1
                    print("Yes")
                    break
            if flag == 1:
                break
            temp_array = []
        if flag == 1:
            break
    if flag == 0:
        print("No")