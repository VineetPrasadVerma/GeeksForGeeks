def jumping_number(number):
    jumping_number_list = []
    for i in range(1, number+1):
        list_of_digits = []
        if i <= 10:
            jumping_number_list.append(i)
            continue
        temp = i
        while temp != 0:
            list_of_digits.append(temp % 10)
            temp //= 10
        for j in range(len(list_of_digits)-1):
            if abs(list_of_digits[j] - list_of_digits[j+1]) != 1:
                break
        else:
            jumping_number_list.append(i)

    return jumping_number_list


t = int(input())
number = []
for _ in range(t):
    number.append(int(input()))
n = max(number)
jumping_list = jumping_number(n)

for n in number:
    difference_list = []
    for i in range(len(jumping_list)+1):
        difference_list.append(abs(i - n))

    index = difference_list.index(min(difference_list))

    for i in range(index):
        print(jumping_list[i], end=" ")

    print()
