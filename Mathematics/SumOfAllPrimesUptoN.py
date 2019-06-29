def prime_no_up_to_n(target):
    list_of_prime = [True] * (target+1)
    list_of_prime[0] = list_of_prime[1] = 0
    temp = 2
    while temp * temp <= target:
        if list_of_prime[temp]:
            for j in range(temp*temp, target+1, temp):
                list_of_prime[j] = False
            temp += 1
    return list_of_prime


numbers = []
for _ in range(int(input())):
    numbers.append(int(input()))
n = max(numbers)
prime_numbers_list = prime_no_up_to_n(n)
total_sum = 0

for i in range(n+1):
    if prime_numbers_list[i]:
        total_sum += i
    prime_numbers_list[i] = total_sum

for n in numbers:
    print(prime_numbers_list[n])

