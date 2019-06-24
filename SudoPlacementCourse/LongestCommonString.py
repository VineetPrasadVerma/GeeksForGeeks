test_cases = int(input())
for _ in range(test_cases):
    first_list = input()
    second_list = input()
    temp = 0
    longest_prefix = ""
    index = 0
    first_substring_list = []
    for i in range(0, len(first_list)):
        first_substring_list.append(first_list[0:i+1])
    #print(first_substring_list)
    for i in first_substring_list:
        if second_list.find(i) != -1 and len(i) > temp:
            index = second_list.find(i)
            longest_prefix = i
            temp = len(i)
    if len(longest_prefix) == 0:
        print(-1)
    else:
        print(index, longest_prefix)