n = int(input())
for _ in range(n):
    size = int(input())
    arr = list(map(int, input().split()))
    rotating_element = int(input())
    ans = arr[rotating_element:] + arr[:rotating_element]
    print(" ".join(str(i) for i in ans))
