import itertools
test_cases = int(input())
for _ in range(test_cases):
    size = int(input())
    prime_list = []
    super_prime_list = []
    count = 0
    for i in range(2, size+1):
        for temp in range(2, i//2):
            if i % temp == 0:
                break
        else:
            if i != 4:
                prime_list.append(i)
                super_prime_list = list(itertools.combinations(prime_list[:prime_list.index(i)], 2))
                for j in super_prime_list:
                    if sum(j) == i:
                        count += 1
                        break
                super_prime_list = []
    print(count)

