def ice_cream_parlor(cost, money):
    a = 0
    b = 0
    limit = len(cost)
    temp = sorted(cost)
    flag = True
    for i in range(limit - 1):
        if flag:
            for j in range(i + 1, limit):
                if temp[i] + temp[j] > money:
                    break
                else:
                    if temp[i] + temp[j] < money:
                        continue
                    elif temp[i] + temp[j] == money:
                        a = temp[i]
                        b = temp[j]
                        flag = False
                        break
        else:
            break
    a = cost.index(a)
    cost[a] = 0
    b = cost.index(b)
    if a+1 > b+1:
        print(b+1, a+1)
    else:
        print(a+1, b+1)


ice_cream_parlor([7, 2, 5, 4, 11], 12)
