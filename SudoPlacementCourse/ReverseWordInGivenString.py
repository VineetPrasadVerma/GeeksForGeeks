test_cases = int(input())
for _ in range(test_cases):
    arr_list = input().split('.')
    for word in range(len(arr_list) - 1, -1, -1):
        if word != 0:
            print(arr_list[word], end=".")
        else:
            print(arr_list[word])

