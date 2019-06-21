def findExtra(a,b,n):
    temp_list = list(set(a) - set(b))
    return a.index(temp_list[0])


print(findExtra([1, 2, 3, 4, 5], [1, 2, 3, 4], 5))
