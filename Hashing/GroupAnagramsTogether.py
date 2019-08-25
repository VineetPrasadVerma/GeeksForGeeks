n = int(input())
for _ in range(n):
    size = int(input())
    sorted_words_list = []
    arr = list(map(str, input().split()))
    for word in arr:
        sorted_words_list.append("".join(sorted(word)))
    freq_word_dict = {}
    for word in sorted_words_list:
        if word not in freq_word_dict:
            freq_word_dict[word] = 1
        else:
            freq_word_dict[word] += 1
    anagrams_count_list = sorted(freq_word_dict.values())
    for i in anagrams_count_list:
        print(i, end=" ")
    print()


