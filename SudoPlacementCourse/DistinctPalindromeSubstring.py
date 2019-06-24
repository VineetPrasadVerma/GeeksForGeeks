test_cases = int(input())
for _ in range(test_cases):
    arr_list = input()
    size = len(arr_list)
    palindrome_list = []
    for i in range(size):
        for j in range(i+1, size+1):
            temp = arr_list[i:j]
            reverse_temp = temp[::-1]
            if temp == reverse_temp:
                palindrome_list.append(temp)
    count = list(set(palindrome_list))
    print(len(count))
