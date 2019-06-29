t = int(input())
for _ in range(t):
    rows, columns = tuple(map(int, input().split()))
    squares = 0
    while rows != 0 and columns != 0:
        squares += rows * columns
        rows -= 1
        columns -= 1
    print(squares)