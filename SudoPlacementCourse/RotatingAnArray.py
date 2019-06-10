n = int(input())

for _ in range(n):
    final_ans_list = []
    size_of_array = int(input())
    array_elements = input()
    rotate_array_element = int(input())

    list_of_elements = [i for i in array_elements.split()]

    list_of_elements = list_of_elements[rotate_array_element:] + list_of_elements[:rotate_array_element]

    string_list_of_elements = [str(i) for i in list_of_elements]
    print(" ".join(string_list_of_elements))

