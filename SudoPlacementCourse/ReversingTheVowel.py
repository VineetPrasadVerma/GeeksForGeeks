test_cases = int(input())
for _ in range(test_cases):
    target = input()
    vowels_list = []
    temp = -1
    for i in target:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            vowels_list.append(i)
    for i in target:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            print(vowels_list[temp], end="")
            temp -= 1
        else:
            print(i, end="")
    print()
