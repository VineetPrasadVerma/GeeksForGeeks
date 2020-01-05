arr1 = [1, 3, 4, 5]
arr2 = [2, 4, 6, 8]
arr3 = arr1[:]
for idx, val in enumerate(arr2):
    for indx, value in enumerate(arr1):
        if val < value:
            arr3.insert(indx, val)
            break
    else:
        arr3.append(val)
print(arr3)