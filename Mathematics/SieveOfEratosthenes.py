t = int(input())
for _ in range(t):
    target = int(input())
    list_up_to_target = [True for i in range(target+1)]
    temp = 2
    while temp * temp <= target:
        if list_up_to_target[temp]:
            for i in range(temp*temp, target+1, temp):
                list_up_to_target[i] = False
        temp += 1

    for i in range(2, target+1):
        if list_up_to_target[i]:
            print(i, end=" ")

    print()

