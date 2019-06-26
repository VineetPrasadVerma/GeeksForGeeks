test_cases = int(input())
for _ in range(test_cases):
    num, l, r = tuple(map(int, input().split()))
    num = int(num)
    l = int(l)
    r = int(r)
    binary_from = list('{0:0b}'.format(num))
    for i in range(len(binary_from) - 1, -1, -1):
        if len(binary_from) - i in range(l, r+1):
            if binary_from[i] == '1':
                binary_from[i] = '0'
            else:
                binary_from[i] = '1'
    string_binary = "".join(binary_from)
    print(int(string_binary, 2))
