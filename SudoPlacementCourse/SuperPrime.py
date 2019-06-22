import itertools
test_cases = int(input())
for _ in range(test_cases):
    size = int(input())
    prime_list = []
    super_prime_list = []
    count = 0
    for i in range(2, size+1):
        flag = False
        temp = 2
        while temp < i:
            if i % temp == 0:
                flag = True
                break
            temp += 1
        if not flag:
            prime_list.append(i)
    super_prime_list = list(itertools.combinations(prime_list, 2))

    for i in prime_list:
        for j in super_prime_list:
            if sum(j) == i:
                count += 1
                break
    print(count)

