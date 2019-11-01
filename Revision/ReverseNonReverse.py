def unique(n):
    if n == 0:
        return
    print(n, end=" ")
    unique(n-1)
    print(n, end=" ")

unique(3)