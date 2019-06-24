test_cases = int(input())
for _ in range(test_cases):
    first_size, second_size = tuple(map(int, input().split()))
    first_list = input()
    second_list = input()
    temp = 0
    first_substring_list = []
    for i in range(first_size):
        for j in range(i+1, first_size+1):
            first_substring_list.append(first_list[i:j])
    for i in first_substring_list:
        if second_list.count(i) > 0 and len(i) > temp:
            temp = len(i)
    print(temp)