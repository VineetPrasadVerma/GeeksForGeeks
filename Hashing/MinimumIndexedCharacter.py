from collections import OrderedDict
n = int(input())
for _ in range(n):
    str_a = input()
    str_b = input()
    word_index_dict = OrderedDict()
    for i in str_b:
        temp = str_a.find(i)
        if temp != -1:
            word_index_dict[i] = temp
        else:
            word_index_dict[i] = 1000000000
    min_val = 100000000
    word = ""
    for key, value in word_index_dict.items():
        if value < min_val:
            min_val = value
            word = key
        if min_val == 100000000:
            word = "$"
    print(word)