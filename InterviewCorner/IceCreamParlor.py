def ice_cream_parlor(cost, money):
    # a = 0
    # b = 0
    # limit = len(cost)
    # temp = sorted(cost)
    # flag = True
    # for i in range(limit - 1):
    #     if flag:
    #         for j in range(i + 1, limit):
    #             if temp[i] + temp[j] > money:
    #                 break
    #             else:
    #                 if temp[i] + temp[j] < money:
    #                     continue
    #                 elif temp[i] + temp[j] == money:
    #                     a = temp[i]
    #                     b = temp[j]
    #                     flag = False
    #                     break
    #     else:
    #         break
    # a = cost.index(a)
    # cost[a] = 0
    # b = cost.index(b)
    # if a+1 > b+1:
    #     print(b+1, a+1)
    # else:
    #     print(a+1, b+1)
    cost_dict = {}
    temp_dict = {}
    a = 0
    b = 0
    for i in cost:
        if i not in cost_dict:
            cost_dict[i] = 1
        else:
            cost_dict[i] += 1
    temp_dict = cost_dict
    if money % 2 == 0:
        if money//2 in cost_dict:
            if cost_dict[money // 2] == 2:
                temp = cost.index(money // 2)
                temp2 = cost.index(money//2, temp+1)
                print(temp+1, temp2+1)
                return
            else:
                for i in cost:
                    temp_dict.pop(i)
                    if money - i in temp_dict:
                        a = i
                        b = money - i
                        break

                temp = cost.index(a)
                temp2 = cost.index(b)
                if temp2 > temp:
                    print(temp + 1, temp2 + 1)
                else:
                    print(temp2 + 1, temp + 1)

                return
        else:
            for i in cost:
                if money - i in cost_dict:
                    a = i
                    b = money - i
                    break

            temp = cost.index(a)
            temp2 = cost.index(b)
            if temp2 > temp:
                print(temp + 1, temp2 + 1)
            else:
                print(temp2 + 1, temp + 1)

            return
    else:
        for i in cost:
            if money - i in cost_dict:
                a = i
                b = money - i
                break
        temp = cost.index(a)
        temp2 = cost.index(b)
        if temp2 > temp:
            print(temp+1, temp2+1)
        else:
            print(temp2+1, temp+1)

        return


ice_cream_parlor([4, 3, 2, 5, 7], 8)
