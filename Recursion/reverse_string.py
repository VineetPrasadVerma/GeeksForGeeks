s = "abc"
reverse_str = ""
for i in range(len(s) - 1, -1, -1):
    reverse_str += s[i]

print(reverse_str)


def reverse_string(s):
    if len(s) == 1:
        return s[0]
    return s[-1] + reverse_string(s[:-1])


print(reverse_string("abc"))