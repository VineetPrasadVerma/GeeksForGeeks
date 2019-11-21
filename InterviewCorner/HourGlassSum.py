arr = [
          [1, 1, 1, 0, 0, 0],
          [0, 1, 0, 0, 0, 0],
          [1, 1, 1, 0, 0, 0],
          [0, 0, 2, 4, 4, 0],
          [0, 0, 0, 2, 0, 0],
          [0, 0, 1, 2, 4, 0]
      ]

lst_hourglass_sum = []


def find_hour_glass_sum(upper_limit, lower_limit):
    temp = 0
    while temp < 4:
        per_hour_glass_sum = 0
        flag = True
        for i in range(upper_limit, lower_limit):
            for j in range(temp, temp+3):
                if flag:
                    per_hour_glass_sum += arr[i][j]
                if not flag:
                    if j == temp + 3 - 2:
                        per_hour_glass_sum += arr[i][j]
            flag = not flag
        lst_hourglass_sum.append(per_hour_glass_sum)
        temp += 1


for i in range(4):
    find_hour_glass_sum(i, i+3)

print(lst_hourglass_sum)