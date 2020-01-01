arr = [100, 4, 200, 1, 208, 207, 2, 3, 6, 5, 102, 103, 205, 206, 209, 104, 105, 106, 107, 108]
arr = sorted(arr)
print(arr)
max_length = 0
longest_length = 0
for i in range(1, len(arr)):
    if arr[i] - arr[i-1] == 1:
        longest_length += 1
    else:
        if max_length < longest_length+1:
            max_length = longest_length+1
        longest_length = 0

    if max_length < longest_length + 1:
        max_length = longest_length + 1
print(max_length)