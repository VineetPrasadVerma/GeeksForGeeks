def no_of_path(m, n):
    if m == 1 or n == 1:
        return 1
    return no_of_path(m-1, n) + no_of_path(m, n-1)


for i in range(int(input())):
    m, n = tuple(map(int, input().split()))
    print(no_of_path(m, n))
