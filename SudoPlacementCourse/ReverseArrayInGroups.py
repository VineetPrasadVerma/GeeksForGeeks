n = int(input())
for _ in range(n):
    final_ans_list = []
    size_of_array_and_groups = input()
    tuple_of_size_and_groups = tuple(map(int, size_of_array_and_groups.split()))
    array_elements = input()
    list_of_elements = [int(i) for i in array_elements.split()]
    list_of_groups = []
    for i in range(0, len(list_of_elements), tuple_of_size_and_groups[-1]):
        list_of_groups.append(list_of_elements[i:i+tuple_of_size_and_groups[-1]])
    for j in list_of_groups:
        final_ans_list.append(j[::-1])

    #print(final_ans_list)
    final_list = []
    for el in final_ans_list:
        final_list.extend(el)

    temp_list = []
    temp_list = [str(i) for i in final_list ]
    print(" ".join(temp_list))



