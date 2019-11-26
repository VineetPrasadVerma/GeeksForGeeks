def checkMagazine(magazine, note):
    magazine_dict = {}
    note_dict = {}
    for m in magazine:
        if m not in magazine_dict:
            magazine_dict[m] = 1
        else:
            magazine_dict[m] += 1

    for n in note:
        if n not in note_dict:
            note_dict[n] = 1
        else:
            note_dict[n] += 1

    for word in note:
        if word not in magazine_dict:
            print("No")
            return
        else:
            if magazine_dict[word] >= 1:
                magazine_dict[word] -= 1
            else:
                print("No")
                return
    print("Yes")


# 6 5
# two times three is not four
# two times two is four

checkMagazine(['two', 'times', 'three', 'is', 'not', 'four'], ['two', 'times', 'two', 'is', 'four'])