def reverse_string(a, temp):
    # temp = ""
    # if len(a) != 0:
    #     temp = a[0]
    #     reverse_string(a[1:])
    # print(temp, end="")
    if a == 0:
        print(temp)
        return
    temp = (temp*10) + a % 10
    reverse_string(a//10, temp)


reverse_string(221, 0)