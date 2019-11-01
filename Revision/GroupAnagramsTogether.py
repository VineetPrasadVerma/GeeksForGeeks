n = int(input())
for _ in range(n):
    size = int(input())
    arr = input().split()
    sorted_arr = []
    for i in arr:
        sorted_arr.append("".join(sorted(i)))
    anagram_dict = {}
    for i in sorted_arr:
        if i not in anagram_dict:
            anagram_dict[i] = 1
        else:
            anagram_dict[i] += 1
    for i in sorted(anagram_dict.values()):
        print(i, end=" ")
    print()
