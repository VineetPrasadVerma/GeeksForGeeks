test_cases = int(input())
for _ in range(test_cases):
    size = int(input())
    arr_list = list(map(int, input().split()))

    max_element = max(arr_list)
    arr_list.remove(max_element)

    print(max(arr_list))