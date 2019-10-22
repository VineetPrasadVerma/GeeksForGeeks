import itertools
n = int(input())
for _ in range(n):
    size = int(input())
    arr = list(map(int, input().split()))
    triplet = itertools.combinations(arr, 3)
    for triple in triplet:
        if triple[0]*triple[0] + triple[1]*triple[1] == triple[2]*triple[2]:
            print(triple)
            print("Yes")
            break
        if triple[1]*triple[1] + triple[2]*triple[2] == triple[0]*triple[0]:
            print(triple)
            print("Yes")
            break
        if triple[0]*triple[0] + triple[2]*triple[2] == triple[1]*triple[1]:
            print(triple)
            print("Yes")
            break
    else:
        print("No")