def reverse(num):
    if num == 0:
        return
    rem = num % 10
    num = num // 10
    if rem != 0:
        print(rem, end="")
    reverse(num)


reverse(122)