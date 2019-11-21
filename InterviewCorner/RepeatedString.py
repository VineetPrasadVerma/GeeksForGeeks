def repeatedString(s, n):
    count_a = s.count("a")
    temp = n % len(s)
    extra_a = s[:temp].count("a")
    return extra_a + count_a * (n//len(s))


print(repeatedString("aba", 10))
