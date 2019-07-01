import itertools
for _ in range(int(input())):
    n = input()
    permute_list = itertools.permutations(n)
    str_permute_list = []
    for i in permute_list:
        str_permute_list.append(int("".join(i)))

    for i in str_permute_list:
        if i % 8 == 0:
            print("Yes")
            break
    else:
        print("No")


