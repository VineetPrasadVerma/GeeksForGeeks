def whatFlavors(cost, money):
    cost_dict = {}
    a = 0
    b = 0
    for i in cost:
        if i not in cost_dict:
            cost_dict[i] = 1
        else:
            cost_dict[i] += 1

    if money % 2 == 0:
        if money//2 in cost_dict:
            if cost_dict[money // 2] == 2:
                temp = cost.index(money // 2)
                temp2 = cost.index(money//2, temp+1)
                print(temp+1, temp2+1)
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
