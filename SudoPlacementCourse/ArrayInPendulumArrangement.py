n = int(input())

for _ in range(n):

    size_of_array = int(input())
    final_ans_list = [0]*size_of_array
    array_elements = input()

    list_of_elements = [int(i) for i in array_elements.split()]

    sorted_list = sorted(list_of_elements)

    #print(sorted_list)

    first_index = 0
    odd_index = 0
    even_index = 0
    if len(list_of_elements) % 2 == 0:
        first_index = int((len(list_of_elements)-1)/2)
    else:
        first_index = int(len(list_of_elements)/2)

    for i in range(0, len(list_of_elements)):
        if i == 0:
            final_ans_list[first_index] = sorted_list[i]
            odd_index = first_index + 1
            even_index = first_index - 1
        elif i % 2 == 0:
            final_ans_list[even_index] = sorted_list[i]
            even_index = even_index - 1
        else:
            final_ans_list[odd_index] = sorted_list[i]
            odd_index = odd_index + 1

    for j in range(len(final_ans_list)):
        print(final_ans_list[j], end=" ")

    print()
