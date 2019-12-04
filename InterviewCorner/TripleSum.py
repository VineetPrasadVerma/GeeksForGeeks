def triplets(a, b, c):
    triplets_lst = []
    for i in a:
        for j in b:
            for k in c:
                if i <= j and j >= k:
                    if (i, j, k) not in triplets_lst:
                        triplets_lst.append((i, j, k))

    return len(triplets_lst)


print(triplets([1, 3, 5, 7], [5, 7, 9], [7, 9, 11, 13]))