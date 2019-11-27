from collections import defaultdict
def freqQuery(queries):
    # ans = []
    # current_dict = {}
    # values_dict = {}
    # for q in queries:
    #     if q[0] == 1:
    #         if q[-1] not in current_dict:
    #             current_dict[q[-1]] = 1
    #             temp = current_dict[q[-1]]
    #             if temp not in values_dict:
    #                 values_dict[temp] = 1
    #             else:
    #                 values_dict[temp] += 1
    #         else:
    #             temp = current_dict[q[-1]]
    #             current_dict[q[-1]] += 1
    #
    #             if temp not in values_dict:
    #                 values_dict[temp] = 1
    #             else:
    #                 values_dict[temp] -= 1
    #
    #             if current_dict[q[-1]] not in values_dict:
    #                 values_dict[current_dict[q[-1]]] = 1
    #             else:
    #                 values_dict[current_dict[q[-1]]] += 1
    #
    #     if q[0] == 2:
    #         if q[-1] in current_dict:
    #             if current_dict[q[-1]] in values_dict:
    #                 values_dict[current_dict[q[-1]]] -= 1
    #                 if values_dict[current_dict[q[-1]]] == 0:
    #                     values_dict.pop(current_dict[q[-1]])
    #                 else:
    #                     if current_dict[q[-1]] - 1 in values_dict:
    #                         values_dict[current_dict[q[-1]] - 1] += 1
    #                     else:
    #                         values_dict[current_dict[q[-1]] - 1] = 1
    #
    #             current_dict[q[-1]] -= 1
    #             if current_dict[q[-1]] == 0:
    #                 current_dict.pop(q[-1])
    #
    #     if q[0] == 3:
    #         if q[-1] in values_dict:
    #             ans.append(1)
    #         else:
    #             ans.append(0)
    #
    # return ans
    elementFreq = {}


# d = {'a': 10, 'b': 20, 'c': 30}
# if 10 in d.items():
#     print("Y")

    elementFreq = defaultdict(int)
    freqCount = defaultdict(int)
    ans = []
    for i, j in queries:
        if i == 1:
            if freqCount[elementFreq[j]]:
                freqCount[elementFreq[j]] -= 1
            elementFreq[j] += 1
            freqCount[elementFreq[j]] += 1
        elif i == 2:
            if elementFreq[j]:
                freqCount[elementFreq[j]] -= 1
                elementFreq[j] -= 1
                freqCount[elementFreq[j]] += 1
        else:
            if j in freqCount and freqCount[j]:
                ans.append(1)
            else:
                ans.append(0)
    return ans