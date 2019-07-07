def get_fibonacci(pos):
    if pos == 0 or pos == 1:
        return pos
    return get_fibonacci(pos - 1) + get_fibonacci(pos - 2)


print(get_fibonacci(9))