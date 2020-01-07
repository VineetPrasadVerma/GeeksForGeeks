arr = [0, 1, 1, 1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 7, 8, 9, 9]
for i in range(len(arr)-1):
    if arr[i] != arr[i+1]:
        print(arr[i], end=" ")
print(arr[-1])

