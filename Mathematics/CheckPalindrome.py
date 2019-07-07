def palindrome(num):
    temp = num
    reversed_int = 0
    while temp != 0:
        rem = temp % 10
        reversed_int = reversed_int * 10 + rem
        temp //= 10
    if num == reversed_int:
        return "Yes"
    else:
        return "No"


print(palindrome(0))
