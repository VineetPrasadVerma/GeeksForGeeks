l = [1, 2, 3, 4]


def reverse_lst(l):
    if l == []:
        return []

    return [l[-1]] + reverse_lst(l[:-1])


print(reverse_lst(l))
