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
    temp = arr[start_index: end_index+1]
    mini = min(temp)
    maxi = max(temp)
    for i in range(start_index):
        if arr[i] > mini:
            start_index = i
            break
    for i in range(length-1, end_index-1, -1):
        if arr[i] < maxi:
            end_index = i
            break
    print(start_index, end_index)


func([10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60])
func([0, 1, 15, 25, 6, 7, 30, 40, 50])
