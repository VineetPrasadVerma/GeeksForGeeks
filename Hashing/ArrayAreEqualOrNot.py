from collections import OrderedDict
test_case = int(input())
for _ in range(test_case):
    size = int(input())
    arr_1 = sorted(list(map(int, input().split())))
    arr_2 = sorted(list(map(int, input().split())))
    # dict_1 = OrderedDict()
    # dict_2 = OrderedDict()
    # for i in arr_1:
    #     if i not in dict_1:
    #         dict_1[i] = 1
    #     else:
    #         dict_1[i] += 1
    # for i in arr_2:
    #     if i not in dict_2:
    #         dict_2[i] = 1
    #     else:
    #         dict_2[i] += 1
    if arr_1 == arr_2:
        print(1)
    else:
        print(0)
