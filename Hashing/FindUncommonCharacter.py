test_case = int(input())
for _ in range(test_case):
    str_a = sorted(set((input())))
    str_b = sorted(set((input())))
    final_ans = []
    for key_a in str_a:
        if key_a not in str_b:
            final_ans.append(key_a)
    for key_b in str_b:
        if key_b not in str_a:
            final_ans.append(key_b)
    ans = "".join(sorted(final_ans))
    print(ans)