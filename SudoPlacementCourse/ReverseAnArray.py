n = int(input())

for _ in range(n):
    final_ans_list = []
    size_of_array = int(input())
    array_elements = input()

    int_list_of_elements = [int(i) for i in array_elements.split()]
    int_list_of_elements = int_list_of_elements[::-1]
    string_list_of_elements = [str(i) for i in int_list_of_elements]
    print(" ".join(string_list_of_elements))
