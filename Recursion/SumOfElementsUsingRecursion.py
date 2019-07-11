def sum_of_elements(l):
    if len(l) == 1:
        return l[0]
    return l[0] + sum_of_elements(l[1:])


print(sum_of_elements([1, 2, 3]))