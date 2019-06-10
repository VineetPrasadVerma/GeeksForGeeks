n = int(input())

for _ in range(n):
    final_ans_list = []
    size_of_array = int(input())
    list_of_elements = input()

    int_list_of_elements = [int(i) for i in list_of_elements.split()]

    for i in range(len(int_list_of_elements)):
        if i == len(int_list_of_elements) - 1:
            final_ans_list.append(int_list_of_elements[i])
            break

        max_element = int_list_of_elements[i]
        temp_max_element = max(int_list_of_elements[i+1:])

        if max_element >= temp_max_element:
            final_ans_list.append(int_list_of_elements[i])

    string_list_of_elements = [str(i) for i in final_ans_list]
    print(" ".join(string_list_of_elements))
