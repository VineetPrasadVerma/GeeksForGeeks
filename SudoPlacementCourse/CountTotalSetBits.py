test_cases = int(input())
for _ in range(test_cases):
    num = int(input())
    count = 0
    for j in range(1, num+1):
        binary_from = list('{0:0b}'.format(j))
        for i in range(len(binary_from)-1, -1, -1):
            if binary_from[i] == '1':
                count += 1
    print(count)