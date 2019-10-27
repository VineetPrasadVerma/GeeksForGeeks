def reverse_digit(num):
    if num == 0:
        return
    else:
        return reverse_digit(num // 10)

print(reverse_digit(123))