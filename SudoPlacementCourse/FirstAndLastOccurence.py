test_cases = int(input())
for _ in range(test_cases):
    final_list = []
    size = int(input())
    arr_list = list(map(int, input().split()))
    element_to_be_searched = int(input())
    for i in range(0, len(arr_list)):
        if arr_list[i] == element_to_be_searched:
            final_list.append(i)
    if final_list == []:
        print(-1)
    else:
        print(final_list[0], final_list[-1])
