def prime_no_up_to_n(target):
    prime_list = []
    list_of_prime = [True] * (target+1)
    list_of_prime[0] = list_of_prime[1] = 0
    temp = 2
    while temp * temp <= target:
        if list_of_prime[temp]:
            for j in range(temp*temp, target+1, temp):
                list_of_prime[j] = False
        temp += 1

    for i in range(2, target+1):
        if list_of_prime[i]:
            prime_list.append(i)
    return prime_list


numbers = []
for _ in range(int(input())):
    numbers.append(int(input()))
n = max(numbers)
prime_numbers_list = prime_no_up_to_n(n)
for i in numbers:
    flag = 0
    for j in range(len(prime_numbers_list)):
        for k in range(len(prime_numbers_list)):
            if prime_numbers_list[j] + prime_numbers_list[k] == i:
                print(prime_numbers_list[j], prime_numbers_list[k])
                flag = 1
                break
        if flag == 1:
            break
