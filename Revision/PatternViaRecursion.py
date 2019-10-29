def pattern(n):
    if n == 1:
        print("*")
        return
    for i in range(n, ):
        print("*", end="")
    print()
    pattern(n-1)


pattern(5)
