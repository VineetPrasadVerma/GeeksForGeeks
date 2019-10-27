n = int(input())
for _ in range(n):
    num = int(input())
    temp = num
    arr = []
    arr.append(num)
    while num > 0:
        arr.append(num-5)
        num -= 5
    while num != temp:
        arr.append(num+5)
        num += 5

    print(arr) 