from collections import OrderedDict
test_case = int(input())
for _ in range(test_case):
    size, k = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    freq_count_dict = OrderedDict()
    for i in arr:
        if i not in freq_count_dict:
            freq_count_dict[i] = 1
        else:
            freq_count_dict[i] += 1
    for key, value in freq_count_dict.items():
        if value == k:
            print(key)
            break
    else:
        print("-1")