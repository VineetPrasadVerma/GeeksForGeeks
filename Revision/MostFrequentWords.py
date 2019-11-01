from collections import OrderedDict
n = int(input())
for _ in range(n):
    size = int(input())
    arr = list(map(str, input().split()))
    freq_count_dict = OrderedDict()
    for word in arr:
        if word not in freq_count_dict:
            freq_count_dict[word] = 1
        else:
            freq_count_dict[word] += 1
    max_freq = -1
    word = []
    for key, value in freq_count_dict.items():
        if value >= max_freq:
            max_freq = value
            word.append(key)
    print(word[-1])
