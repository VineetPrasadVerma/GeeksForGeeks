n = int(input())
for _ in range(n):
    size = int(input())
    s = input()
    rev_lst = []
    for i in range(size-1, -1, -1):
        rev_lst.append(s[i])
    rev_s = "".join(k for k in rev_lst)
    if s == rev_s:
        print("Yes")
    else:
        print("No")