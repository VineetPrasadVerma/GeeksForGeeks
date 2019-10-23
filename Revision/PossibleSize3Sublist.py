import math
# def choose_sets_help(lst, k, ans):
#     ''' Input: lst,
#         Output: a list of all k-length sub-lists '''
#     if len(lst) == k:
#         if lst not in ans:
#             ans.append(lst)
#         return ans
#     if len(lst) < k or k == 0:
#         return [[]]
#     for elm in lst:
#         sub_lst = lst[:]
#         sub_lst.remove(elm)
#         choose_sets_help(sub_lst, k, ans)
#     return ans
#
#
# def choose_sets(lst, k):
#     return choose_sets_help(lst, k, [])
#
# print(choose_sets([1,2,3,4,5], 3))


def possible_sublist_help(lst, window, ans, max_limit):
    if len(ans) == max_limit:
        return ans

    if len(lst) == window:
        if lst not in ans:
            ans.append(lst)
        return ans

    if len(lst) < window or window == 0:
        return [[]]

    for elm in lst:
        sub_lst = lst[:]
        sub_lst.remove(elm)
        possible_sublist_help(sub_lst, window, ans, max_limit)
    return ans


def possible_sublist(lst, window):
    length = len(lst)
    upper_bound = int(math.factorial(length)/(math.factorial(window) * math.factorial(length - window)))
    print(upper_bound)
    return possible_sublist_help(lst, window, [], upper_bound)

print(possible_sublist([1,2,3,4,5], 3))