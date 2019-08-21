n = int(input())
for _ in range(n):
    ans = 1
    word = input()
    each_word_count = {}
    for i in word:
        if i not in each_word_count:
            each_word_count[i] = 1
        else:
            ans = 0
            break

    print(ans)


