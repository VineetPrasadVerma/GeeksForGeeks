def isInterleave(A, B, C):
    index_list = []
    next_index = 0
    i = sorted(A+B)
    j = sorted(C)
    if i != j:
        return 0
    for letter in A:
        next_index = C.find(letter, next_index)
        if next_index == -1:
            return 0
        index_list.append(next_index)
        next_index += 1
    if sorted(index_list) == index_list:
        pass
    else:
        return 0
    for i in index_list:
        C = C[:i] + C[i+1:]
    next_index = 0
    index_list = []
    for letter in B:
        next_index = C.find(letter, next_index)
        if next_index == -1:
            return 0
        index_list.append(next_index)
        next_index += 1
    if sorted(index_list) == index_list:
        return 1
    else:
        return 0

print(isInterleave('aab',  'axy ',  'aaxaby'))