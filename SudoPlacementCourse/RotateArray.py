n = int(input())
for _ in range(n):
    final_ans_list = []
    size_of_array_and_rotation_size = input()
    int_list_size_of_array_and_rotation_size = [int(i) for i in size_of_array_and_rotation_size.split()]
    array_elements = input()

    list_of_elements = [i for i in array_elements.split()]

    list_of_elements = list_of_elements[int_list_size_of_array_and_rotation_size[-1]:] + list_of_elements[:int_list_size_of_array_and_rotation_size[-1]]

    string_list_of_elements = [str(i) for i in list_of_elements]
    print(" ".join(string_list_of_elements))

