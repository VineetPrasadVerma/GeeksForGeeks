test_cases = int(input())
for _ in range(test_cases):
    arr_list = input()
    ans = ""
    size = len(arr_list)
    substring_list = []
    for i in range(size):
        for j in range(i+1, size+1):
            substring_list.append(arr_list[i:j])
    temp = 0
    for i in substring_list:
        if i == i[::-1] and len(i) > temp:
            ans = i
            temp = len(i)
    print(ans)