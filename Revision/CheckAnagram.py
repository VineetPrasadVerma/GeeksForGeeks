n = int(input())
for _ in range(n):
    str1, str2 = tuple(map(str, input().split()))
    if sorted(str1) == sorted(str2):
        print("YES")
    else:
        print("NO")