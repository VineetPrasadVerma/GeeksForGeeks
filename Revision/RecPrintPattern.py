def print_pattern(num):
    if num < 0:
        print(num, end=" ")
        return
    print(num, end=" ")
    print_pattern(num-5)

    print(num, end=" ")


print_pattern(16)