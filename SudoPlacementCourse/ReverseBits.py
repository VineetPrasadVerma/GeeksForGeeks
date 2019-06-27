for _ in range(int(input())):
    n = int(input())
    binary_num = '{0:032b}'.format(n)
    binary_num = binary_num[::-1]
    decimal_from = int(binary_num, 2)
    print(decimal_from)