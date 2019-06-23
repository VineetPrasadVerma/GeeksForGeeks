test_cases = int(input())
for _ in range(test_cases):
    first_size, second_size = tuple(map(int, input().split()))
    first_list = list(map(int, input().split()))
    second_list = list(map(int, input().split()))
    target = int(input())
    sorted_first_array = sorted(first_list)
    sorted_second_array = sorted(second_list)
    minimum_difference = 100000000000
    tuple_ans = ()
    for i in sorted_second_array[::-1]:
        for j in sorted_first_array[::-1]:
            if minimum_difference > abs(target-(i+j)):
                minimum_difference = abs(target-(i+j))
                tuple_ans = j, i

    print(str(tuple_ans[0])+" "+str(tuple_ans[-1]))
