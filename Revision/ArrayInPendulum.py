n = int(input())
for _ in range(n):
    size = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = sorted(arr)
    ans_list = [] * size
    temp = int((size - 1) / 2)
    for i in range(size):
        if i == 0:
            ans_list.insert(temp, sorted_arr[i])
        if i % 2 != 0:
            temp = temp + i
            ans_list.insert(temp, sorted_arr[i])
        else:
            temp = temp - i
            ans_list.insert(temp, sorted_arr[i])
    print(ans_list)
