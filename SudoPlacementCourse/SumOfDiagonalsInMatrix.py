def sum_of_diagonals(l):
    sums = 0
    for i in range(len(l)):
        for j in range(len(l)):
            if i == j:
                sums += l[i][j]
    return sums


print(sum_of_diagonals([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
