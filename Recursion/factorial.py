# n = int(input())
#
# ans = 1
# for i in range(n, 0, -1):
#     ans *= i
# print(ans)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


print(fact(600))
