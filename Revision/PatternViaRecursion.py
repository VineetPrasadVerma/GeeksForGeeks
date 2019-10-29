def pattern(temp, n):
    if temp == n+1:
        return
    for i in range(temp):
        print("*", end = "")
    print()
    pattern(temp+1, n)



pattern(1, 5)
