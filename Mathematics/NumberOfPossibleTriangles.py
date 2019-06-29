import itertools
t = int(input())
for _ in range(t):
    size = int(input())
    possible_triangle = 0
    arr = list(map(int, input().split()))
    possible_triangle_list = itertools.combinations(arr, 3)

    for triangle in possible_triangle_list:
        # print(triangle)
        if triangle[0] + triangle[1] > triangle[2]:
            if triangle[0] + triangle[2] > triangle[1]:
                if triangle[1] + triangle[2] > triangle[0]:
                    possible_triangle += 1
    print(possible_triangle)