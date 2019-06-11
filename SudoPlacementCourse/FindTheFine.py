n = int(input())
for _ in range(n):
    final_ans_list = []
    size_of_array_and_date = input()
    int_list_size_of_array_and_date = [int(i) for i in size_of_array_and_date.split()]
    car_numbers_list = input()
    list_of_car_numbers = [int(i) for i in car_numbers_list.split()]
    fine_list = input()
    list_of_fines = [int(i) for i in fine_list.split()]
    date = int_list_size_of_array_and_date[-1]
    if date % 2 == 0:
        for i in range(0, len(list_of_car_numbers)):
            if list_of_car_numbers[i] % 2 != 0:
                final_ans_list.append(list_of_fines[i])
    else:
        for i in range(0, len(list_of_car_numbers)):
            if list_of_car_numbers[i] % 2 == 0:
                final_ans_list.append(list_of_fines[i])
    print(sum(final_ans_list))
