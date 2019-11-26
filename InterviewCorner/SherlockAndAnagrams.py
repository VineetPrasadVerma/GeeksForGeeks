def sherlockAndAnagrams(s):
    sub_str_lst = []
    for i in range(1, len(s)):
        temp = []
        for j in range(len(s) - i + 1):
            temp.append("".join(sorted(s[j:j+i])))
        sub_str_lst.append(temp)

    #print(sub_str_lst)
    total_anagrams = 0
    for lst in sub_str_lst:
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[i] == lst[j]:
                    total_anagrams += 1
    print(total_anagrams)
sherlockAndAnagrams("cdcd")