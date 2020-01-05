arr1 = [1, 3, 4, 5, 10, 232]
arr2 = [2, 4, 6, 8, 9, 12313]
a1_length = len(arr1)
a2_length = len(arr2)
i = j = 0
arr3 = []
# arr3 = arr1[:]
# for idx, val in enumerate(arr2):
#     for indx, value in enumerate(arr1):
#         if val < value:
#             arr3.insert(indx, val)
#             break
#     else:
#         arr3.append(val)
# print(arr3)

# by using merge sort
while i < a1_length and j < a2_length:
    if arr1[i] <= arr2[j]:
        arr3.append(arr1[i])
        i += 1
    else:
        arr3.append(arr2[j])
        j += 1

if i == a1_length:
    arr3 += arr2[j:]
else:
    arr3 += arr1[i:]

print(arr3)

