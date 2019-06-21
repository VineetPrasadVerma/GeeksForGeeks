def bin_search(arr, left, high, key):
    flag = 0
    left = 0
    high = len(arr)-1
    while left <= high:
        mid = int((left + high) / 2)
        if arr[mid] == key:
            flag = 1
            return mid
            break
        elif arr[mid] > key:
            high = mid - 1
        else:
            left = mid + 1
    if flag == 0:
        return -1

bin_search([1, 2, 5,8,9,10,11,12,13,14,16,17], 0, 7, 14)