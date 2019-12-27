def func(arr):
    start_index = 0
    end_index = 0
    length = len(arr)
    for i in range(0, length - 1):
        if arr[i] > arr[i+1]:
            start_index = i
            end_index = i+1
            break
    for i in range(length-1, 0, -1):
        if arr[i] < arr[i-1]:
            end_index = i
            break

    print(start_index, end_index)


func([10, 3, 2, 5, 4, 6])
