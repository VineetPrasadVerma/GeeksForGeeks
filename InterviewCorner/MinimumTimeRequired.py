def minTime(machines, goal):
    produced_items = 0
    days = 0
    while produced_items < goal:
        days += 1
        temp = 0
        for i in machines:
            if days % i == 0:
                temp += 1

        produced_items += temp

    return days


print(minTime([2, 3, 2], 10))
