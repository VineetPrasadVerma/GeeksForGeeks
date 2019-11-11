def copystr(s1, s2, index):
    if s1 == "":
        return ""
    s2[index] = s1[0]
    index += 1
    return copystr(s1[1:], s2, index)


s1 = "Hello"
s2 = [""] * len(s1)
copystr(s1, s2, 0)
print(s2)