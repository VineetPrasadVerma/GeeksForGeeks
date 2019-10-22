import itertools
test_cases = int(input())
for i in range(0, test_cases):
    no_of_digits = int(input())
    list_of_digits = input()
    int_list_of_digits = list(map(int, list_of_digits.split()))
    str_list_of_digits = []
    dicts = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }

    for i in int_list_of_digits:
        str_list_of_digits.append(dicts[i])

    ans_list = itertools.product(* str_list_of_digits)

    for first in ans_list:
        for j in first:
            print(j, end="")
        print(end=" ")
