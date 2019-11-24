def mini_swap(arr):
    total_swap = 0
    i = 0
    while i < len(arr):
        if arr[i] != i+1:
            temp = arr[i]
            arr[i], arr[temp - 1] = arr[temp - 1], arr[i]
            total_swap += 1
        else:
            i += 1
    return total_swap


print(mini_swap([4, 3, 1, 2]))