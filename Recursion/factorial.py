# n = int(input())
#
# ans = 1
# for i in range(n, 0, -1):
#     ans *= i
# print(ans)

#Factorial
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
#
#
# print(fact(600))


#reverse
# def reverse(s):
#     if s == "":
#         return ""
#     return s[-1] + reverse(s[:-1])
#
#
# print(reverse("Hello Vineet"))


#Print Pattern Recusively
def print_pattern(n):
    if n == 1:
        print('*')
        return
    else:
        temp = n
        while temp <= n:
            print('*',  end="")
            temp += 1
        print()
        print_pattern(n-1)


print_pattern(10)