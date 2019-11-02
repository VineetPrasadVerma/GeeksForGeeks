# n = int(input())
# for _ in range(n):
#     count = 0
#     size = int(input())
#     arr = list(map(int, input().split()))
#     sub_arr = []
#     # for i in range(size):
#     #     for j in range(i+1, size + 1):
#     #         sub_arr.append(arr[i:j])
#     # print(len(sub_arr))
#     # for lst in sub_arr:
#     #     if sum(lst) == 0:
#     #         count += 1
#     # print(count)
#
#     for i in range(size):
#         total = 0
#         for j in range(i, size):
#             total += arr[j]
#             if total == 0:
#                 count += 1
#     print(count)

# n = int(input())
# for _ in range(n):
#     count = 0
#     size = int(input())
#     arr = list(map(int, input().split()))
#     curr_sum = arr[0]
#     start = 0
#     end = 0
#     while start != size:
#         if end == size-1:
#             start += 1
#         if curr_sum == 0:
#             count += 1
#             end += 1
#             curr_sum += arr[end]
#         elif curr_sum < 0:
#             end += 1
#             curr_sum += arr[end]
#         else:
#             while curr_sum > 0 and start <= end:
#                 curr_sum -= arr[start]
#                 start += 1
#     print(count)


def sub_array_with_sum_zero(arr, n):
    different_sum_dict = {}
    sub_array_indices_list = []
    cumulative_sum = 0

    for i in range(n):
        cumulative_sum += arr[i]

        if cumulative_sum == 0:
            sub_array_indices_list.append((0, i))

        temp_list = []
        if cumulative_sum in different_sum_dict:
            temp_list = different_sum_dict[cumulative_sum]
            for j in range(len(temp_list)):
                sub_array_indices_list.append((temp_list[j] + 1, i))

        temp_list.append(i)
        different_sum_dict[cumulative_sum] = temp_list

    return sub_array_indices_list


n = int(input())
for _ in range(n):
    count = 0
    size = int(input())
    arr = list(map(int, input().split()))
    print(len(sub_array_with_sum_zero(arr, size)))


