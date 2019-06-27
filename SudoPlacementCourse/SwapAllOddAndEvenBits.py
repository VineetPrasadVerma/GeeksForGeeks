test_cases = int(input())
for _ in range(test_cases):
    num = int(input())
    binary_num = '{0:08b}'.format(num)
    ans_list = []
    for i in range(0, len(binary_num)-1, 2):
        ans_list.append(binary_num[i+1])
        ans_list.append(binary_num[i])
    ans_string = "".join(ans_list)
    print(int(ans_string, 2))
