n = int(input())

for _ in range(n):
    final_ans_list = []
    size_of_array = int(input())
    array_elements = input()

    int_list_of_elements = [int(i) for i in array_elements.split()]

    for i in range(len(int_list_of_elements)):
        if i == len(int_list_of_elements) - 1:
            final_ans_list.append(-1)
        else:
            if int_list_of_elements[i + 1] < int_list_of_elements[i]:
                final_ans_list.append(int_list_of_elements[i + 1])
            else:
                final_ans_list.append(-1)

    string_list_of_elements = [str(i) for i in final_ans_list]
    print(" ".join(string_list_of_elements))
