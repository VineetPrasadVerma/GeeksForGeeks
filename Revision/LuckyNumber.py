n = int(input())
for _ in range(n):
    num = input()
    length = len(num)
    sub_numbers = []
    for i in range(length):
        for j in range(i+1, length+1):
            sub_numbers.append(num[i:j])
    lst = []
    for elm in sub_numbers:
        temp = 1
        for i in elm:
            temp *= int(i)
        lst.append(temp)
    if len(lst) == len(set(lst)):
        print(1)
    else:
        print(0)
