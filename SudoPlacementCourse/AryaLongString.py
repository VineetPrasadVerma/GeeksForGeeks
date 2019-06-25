test_cases = int(input())
for _ in range(test_cases):
    string = input()
    times, target, word = tuple(map(str, input().split()))
    times = int(times)
    target = int(target)
    word = str(word)
    word_count = 0
    # arya_str = ""
    # for i in range(times):
    #     arya_str += string
    # for i in range(target):
    #     if arya_str[i] == word:
    #         ans += 1
    # print(ans)
    for i in string:
        if i == word:
            word_count += 1
    temp = 0
    remaining_element = target % len(string)
    total_sets = target - remaining_element
    total_sets = total_sets // len(string)
    for i in range(remaining_element):
        if string[i] == word:
            temp += 1
    print((total_sets * word_count) + temp)
