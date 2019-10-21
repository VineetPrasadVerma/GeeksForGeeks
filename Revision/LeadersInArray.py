def leaders_in_array():
    n = int(input())
    for _ in range(n):
        size = int(input())
        arr = list(map(int, input().split()))
        maximum = -1
        ans_list = []
        for i in range(size-1, -1, -1):
            if arr[i] >= maximum:
                maximum = arr[i]
                ans_list.append(maximum)
        for j in ans_list[::-1]:
            print(j, end=" ")
        print()


leaders_in_array()

