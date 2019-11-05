def tour(lis, n):
    petrol_lst = []
    distance_lst = []
    for lst in lis:
        petrol_lst.append(lst[0])
        distance_lst.append(lst[-1])

    flag = False
    for i in range(n):
        deficit_petrol = 0
        remaining_petrol = 0
        start = i
        count = 0
        for j in range(i, i+n):
            temp = j % n
            if petrol_lst[temp] - distance_lst[temp] >= 0:
                remaining_petrol += petrol_lst[temp] - distance_lst[temp]
            else:
                deficit_petrol = abs(petrol_lst[temp] - distance_lst[temp])
                if remaining_petrol - deficit_petrol >= 0:
                    remaining_petrol = remaining_petrol - deficit_petrol
                else:
                    break
            count += 1
        if count == n:
            flag = True
            print(start)
            break
    if not flag:
        print(-1)



tour([[4, 6], [6, 5], [7, 3], [4, 5]], 4)
