def alone_in_a_group(arr):
    length = len(arr)
    if arr[-1] != arr[-2]:
        return arr[-1]

    for i in range(0, length-1):
        if arr[i] != arr[i+1]:
            if arr[i] != arr[i-1]:
                return arr[i]


print(alone_in_a_group([1, 2, 2, 2, 3, 3, 4, 4, 5, 5]))

