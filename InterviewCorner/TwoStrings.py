def twoStrings(s1, s2):
    first_dict = {}

    for i in s1:
        if i not in first_dict:
            first_dict[i] = 1
        else:
            first_dict[i] += 1

    for i in s2:
        if i in first_dict:
            return "YES"
    return "NO"
