n = int(input())

for _ in range(n):
    final_ans_list = []
    size_of_array = int(input())
    list_of_elements = input()
    int_list_of_elements = [int(i) for i in list_of_elements.split()]
    list_of_even_elements = []
    list_of_odd_elements = []
    for i in range(len(int_list_of_elements)):
        if int_list_of_elements[i] % 2 == 0:
            list_of_even_elements.append(int_list_of_elements[i])
        else:
            list_of_odd_elements.append(int_list_of_elements[i])
    final_ans_list = sorted(list_of_odd_elements, reverse=True) + sorted(list_of_even_elements)

    for i in final_ans_list:
        print(i, end=" ")
    print()
