import itertools
test_cases = int(input())
for i in range(0, test_cases):
    no_of_digits = int(input())
    list_of_digits = input()
    int_list_of_digits = list(map(int, list_of_digits.split()))
    str_list_of_digits = []
    for i in int_list_of_digits:
        if i == 2:
            str_list_of_digits.append(['a', 'b', 'c'])
        elif i == 3:
            str_list_of_digits.append(['d', 'e', 'f'])
        elif i == 4:
            str_list_of_digits.append(['g', 'h', 'i'])
        elif i == 5:
            str_list_of_digits.append(['j', 'k', 'l'])
        elif i == 6:
            str_list_of_digits.append(['m', 'n', 'o'])
        elif i == 7:
            str_list_of_digits.append(['p', 'q', 'r', 's'])
        elif i == 8:
            str_list_of_digits.append(['t', 'u', 'v'])
        elif i == 9:
            str_list_of_digits.append(['w', 'x', 'y', 'z'])
    final_ans_list = itertools.product(*str_list_of_digits)
    for element in final_ans_list:
        print("".join(element), end=" ")
    print()