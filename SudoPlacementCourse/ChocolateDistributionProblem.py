n = int(input())
for _ in range(n):
    no_of_packet = int(input())
    final_ans_list = []
    array_elements = input()
    list_of_elements = [int(i) for i in array_elements.split()]
    no_of_students = int(input())
    sorted_list_of_elements = sorted(list_of_elements)
    for i in range(0, (len(list_of_elements) - no_of_students)+1):
        final_ans_list.append(sorted_list_of_elements[(i+no_of_students)-1] - sorted_list_of_elements[i])
    print(min(final_ans_list, default=0))
