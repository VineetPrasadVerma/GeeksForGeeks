test_cases = int(input())
for _ in range(test_cases):
    num = int(input())
    binary_from = list('{0:0b}'.format(num))
    for i in range(len(binary_from)-1, -1, -1):
        if binary_from[i] == '1':
            print(len(binary_from)-i)
            break
    else:
        print(0)