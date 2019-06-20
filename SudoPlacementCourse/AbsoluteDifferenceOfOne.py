    test_cases = int(input())
    for _ in range(test_cases):
        size, num = tuple(map(int, input().split()))
        arr_list = list(map(int, input().split()))
        reduced_list = []
        final_list = []
        for i in arr_list:
            if i < num:
                reduced_list.append(i)

        for i in reduced_list:
            temp = i
            prev_digit = -1
            while temp:
                curr_digit = temp % 10
                if prev_digit == -1:
                    prev_digit = curr_digit
                else:
                    if abs(prev_digit - curr_digit) == 1:
                        prev_digit = curr_digit
                        if temp == int(str(i)[0]):
                            final_list.append(i)
                    else:
                        break

                temp = int(temp/10)
        if len(final_list) == 0:
            print(-1)
        else:
            print(" ".join(str(i) for i in final_list))

