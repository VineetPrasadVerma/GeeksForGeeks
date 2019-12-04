def triplets(a, b, c):
    # triplets_lst = []
    # for i in a:
    #     for j in b:
    #         for k in c:
    #             if i <= j and j >= k:
    #                 if (i, j, k) not in triplets_lst:
    #                     triplets_lst.append((i, j, k))
    #
    # return len(triplets_lst)

    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))

    ai = 0
    bi = 0
    ci = 0
    ans = 0

    while bi < len(b):
        while ai < len(a) and a[ai] <= b[bi]:
            ai += 1

        while ci < len(c) and c[ci] <= b[bi]:
            ci += 1

        ans += ai * ci
        bi += 1

    return ans


print(triplets([1, 3, 5, 7], [5, 7, 9], [7, 9, 11, 13]))