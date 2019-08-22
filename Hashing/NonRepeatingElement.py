from collections import OrderedDict
test_cases = int(input())
for _ in range(test_cases):
    size = int(input())
    arr = list(map(int, input().split()))
    freq_dict = OrderedDict()
    for i in arr:
        if i not in freq_dict:
            freq_dict[i] = 1
        else:
            freq_dict[i] += 1
    print(freq_dict)
    for key, value in freq_dict.items():
        if value == 1:
            print(key)
            break
    else:
        print(0)
