arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# max_sum_of_sub_array = 0
# for i in range(len(arr)):
#     for j in range(1, len(arr)):
#         if j - i == 1:
#             current_sum = arr[i] + arr[j]
#         current_sum += arr[j]
#     if max_sum_of_sub_array < current_sum:
#         max_sum_of_sub_array = current_sum
#     current_sum = 0
#
# print(max_sum_of_sub_array)

max_ending_here = max_so_far = 0
for i in range(len(arr)):
    max_ending_here += arr[i]
    if max_ending_here < 0:
        max_ending_here = 0
    if max_so_far < max_ending_here:
        max_so_far = max_ending_here

print(max_so_far)



