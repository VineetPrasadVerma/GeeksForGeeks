test_cases = int(input())
for _ in range(test_cases):
    flag = 0
    arr_list = input()
    for i in range(0, len(arr_list)):
        if (arr_list[i] == 'a' or arr_list[i] == 'e' or arr_list[i] == 'i' or arr_list[i] == 'o'
                or arr_list[i] == 'u' or arr_list[i] == 'A' or arr_list[i] == 'E'
                or arr_list[i] == 'I' or arr_list[i] == 'O' or arr_list[i] == 'U'):
            flag = 1
            print(arr_list[i], end="")
        elif arr_list[i] == ' ':
            print(arr_list[i], end="")

    if flag == 0:
        print("No Vowel")
    else:
        print()