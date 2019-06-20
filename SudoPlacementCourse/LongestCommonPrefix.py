test_cases = int(input())
for _ in range(test_cases):
    flag = 0
    k = 0
    size = int(input())
    arr_list = input().split()
    sorted_array = sorted(arr_list, key = len)
    #print(sorted_array)
    first_element = sorted_array[0]
    temp = first_element
    while k < len(first_element):
        flag = 0
        k += 1
        for i in range(1, size):
            if sorted_array[i].startswith(temp):
                continue
            else:
                flag = 1
                temp = temp[:-1]
                break
    if flag == 1:
        print(-1)
    else:
        print(temp)
