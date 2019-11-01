n = int(input())
for _ in range(n):
    size, window = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    sub_arr =[]
    for i in range(0, size-window+1):
        sub_arr.append(arr[i: i+window])
    for lst in sub_arr:
        count_dict = {}
        for elm in lst:
            if elm not in count_dict:
                count_dict[elm] = 1
            else:
                count_dict[elm] += 1
        print(len(count_dict.keys()), end=" ")
    print()
