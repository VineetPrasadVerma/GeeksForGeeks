def print_pattern(n):
    global reached_zero
    global starting_value_count
    if n == starting_value:
        starting_value_count += 1
    print(n, end=" ")

    if n > 0 and not reached_zero:
        print_pattern(n-5)
    elif starting_value_count < 2:
        reached_zero = True
        print_pattern(n+5)


n = int(input())
reached_zero = False
starting_value_count = 0
starting_value = n
print_pattern(n)