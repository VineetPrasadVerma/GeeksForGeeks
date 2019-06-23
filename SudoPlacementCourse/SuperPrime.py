import math
test_cases = int(input())
size = []
for _ in range(0, test_cases):
    size.append(int(input()))
limit = max(size) + 1
prime_list = limit * [None]
for i in range(2, limit+1):
    for temp in range(2, int(math.sqrt(i)) + 1):
        if i % temp == 0:
            break
    else:
        prime_list[i] = True

for i in size:
    count = 0
    for j in range(i-1):
        if prime_list[j] and prime_list[j+2]:
            count += 1
    print(count)

