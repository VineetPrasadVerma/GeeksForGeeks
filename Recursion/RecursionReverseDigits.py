def reverse_digits(n):
    global ans
    rem = n % 10
    n //= 10
    if n != 0:
        ans += str(rem)
        reverse_digits(n)
    else:
        ans += str(rem)


n = int(input())
ans = ""
reverse_digits(n)
print(int(ans))