n = int(input())
for _ in range(n):
    size_of_array_and_closest_number = input()
    int_size_of_array_and_closest_number = [int(i) for i in size_of_array_and_closest_number.split()]
    array_elements = input()

    list_of_elements = [int(i) for i in array_elements.split()]

    closest_value = 0
    minimum_difference = 10000000000000
    for i in range(len(list_of_elements)):
        if minimum_difference >= abs(list_of_elements[i]-int_size_of_array_and_closest_number[-1]):
            minimum_difference = abs(list_of_elements[i]-int_size_of_array_and_closest_number[-1])

            closest_value = list_of_elements[i]

    print(closest_value)
