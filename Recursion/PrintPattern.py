# for _ in range(int(input())):
#     n = int(input())
#     final_list = [n]
#     temp = n
#
#     while temp > 0:
#         final_list.append(temp - 5)
#         temp -= 5
#
#     while temp < n:
#         final_list.append(temp + 5)
#         temp += 5
#
#     print(" ".join(str(i) for i in final_list))


def print_pattern(target, temp):
    if target > 0:
        print(target, end=' ')
        print_pattern(target-5, temp)

    print(target, end=' ')


n = int(input())
for i in range(n):
    target = int(input())
    temp = target
    print_pattern(target, temp)
    print()

