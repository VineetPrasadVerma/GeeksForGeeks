def perm(strng):
    if len(strng) == 0:
        return ""
    elif len(strng) == 1:
        return strng
    else:
        lst = []
        for i in range(len(strng)):
            x = strng[i]
            xs = strng[:i] + strng[i + 1:]
            for p in perm(xs):
                lst.append(x + p)
        return lst


for item in perm("abcd"):
    print(item, end=" ")
print()
