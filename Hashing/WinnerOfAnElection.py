n = int(input())
for _ in range(n):
    no_of_votes = int(input())
    vote_list = list(map(str, input().split()))
    dict_votes_for_each_voters = {}
    for i in vote_list:
        if i not in dict_votes_for_each_voters:
            dict_votes_for_each_voters[i] = 1
        else:
            dict_votes_for_each_voters[i] += 1
    max_value = max(dict_votes_for_each_voters.values())
    final_ans = [key for key, value in dict_votes_for_each_voters.items() if value == max_value]
    print(sorted(final_ans)[0], end=" "+str(max_value))
    print()


