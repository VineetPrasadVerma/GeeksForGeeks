def substring(s):
    ans = []
    if s == "":
        return ans
    for i in range(len(s)):
        temp = s[:i+1]
        if temp[0] == temp[-1]:
            ans.append(temp)
    return ans + substring(s[1:])


print(substring("abcab"))