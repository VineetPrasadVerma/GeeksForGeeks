def count_distinct(arr, n, k):
    for i in range(0, (len(arr) - k + 1)):
        print(len(set(arr[i:i+k])), end=" ")


count_distinct([78,16, 94, 36,87,93,50,22,63,28,91,60,64,27], 14, 5)
