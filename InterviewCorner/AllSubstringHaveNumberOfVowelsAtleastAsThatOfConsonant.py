word = input()
flag = 0
for i in range(1, len(word)):
    if (word[i-1] != "a" or word[i-1] != "e" or word[i-1] != "i" or word[i-1] != "o" or word[i-1] != "u") and\
            (word[i] != "a" or word[i-1] != "e" or word[i-1] != "i" or word[i-1] != "o" or word[i-1] != "u"):
        print(False)
        flag = 1
        break

if flag == 0:
    for i in range(1, len(word) - 1):
        if (word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u") \
                and (word[i - 1] != "a" or word[i - 1] != "e" or word[i - 1] != "i" or word[i - 1] != "o" or word[i - 1] != "u")\
                    and (word[i + 1] != "a" or word[i + 1] != "e" or word[i + 1] != "i" or word[i + 1] != "o" or word[i + 1] != "u") :
            print(False)
            flag = 1
            break

if flag == 0:
    print(True)
