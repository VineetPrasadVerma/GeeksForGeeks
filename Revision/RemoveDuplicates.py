from collections import OrderedDict
n = int(input())
for _ in range(n):
    word = input()
    letters_dict = OrderedDict()
    for i in word:
        if word not in letters_dict:
            letters_dict[i] = 1
    print("".join(letters_dict.keys()))