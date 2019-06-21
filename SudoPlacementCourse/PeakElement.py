def peakElement(arr, n):
    for i in range(n):
        if n == 1:
            return i
            break
        elif i == 0:
            if arr[i] > arr[i+1]:
                return i
                break
        elif i == n-1:
            if arr[i] > arr[i-1]:
                return i
                break
        else:
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                return i
                break


print(peakElement([1, 2, 3], 3))