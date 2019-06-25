numbers_list = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
romans_list = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']


def convert_roman(n):
    ans = ""
    for i in range(12, -1, -1):
        while n >= numbers_list[i] and n != 0:
            ans += romans_list[i]
            n = n - numbers_list[i]

    return ans

print(convert_roman(400))