test_cases = int(input())
for _ in range(test_cases):
    size, no_of_query = input().split()
    input_string = input()
    no_of_query = int(no_of_query)
    types_of_operation = []
    for i in range(no_of_query):
        types_of_operation.append(tuple(map(int, input().split())))
    for j in types_of_operation:
        if j[0] == 1:
            temp = j[-1]
            if j[-1] > int(size):
                temp = j[-1] % int(size)
            input_string = input_string[int(size)-temp:] + input_string[0:int(size)-temp]
            print(input_string)
        else:
            print(input_string[j[-1]])
