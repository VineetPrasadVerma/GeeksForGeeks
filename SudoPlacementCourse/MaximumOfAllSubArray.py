test_cases = int(input())
for _ in range(test_cases):
    list_size_and_sub_array_size = list(map(int, input().split()))
    window = list_size_and_sub_array_size[-1]
    int_list_of_digits = list(map(int, input().split()))
    # list_of_max_subarray = []
    # for i in range(0, (len(int_list_of_digits)-window)+1):
    #     list_of_max_subarray.append(max(int_list_of_digits[i:i + window]))
    # print(" ".join(str(i) for i in list_of_max_subarray))
    max = 0

    for i in range((len(int_list_of_digits)-window)+1):
        max = int_list_of_digits[i]
        for j in range(1, window):
            if int_list_of_digits[i + j] > max:
                max = int_list_of_digits[i + j]
        print(str(max) + " ", end="")
    print()