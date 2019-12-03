def pairs(k, arr):
    count = 0
    temp_dict = {}
    for i in arr:
        if i not in temp_dict:
            temp_dict[i] = 1

    for i in arr:
        if i + k in temp_dict:
            count += 1

    return count


print(pairs(2, [1, 5, 3, 4, 2]))
