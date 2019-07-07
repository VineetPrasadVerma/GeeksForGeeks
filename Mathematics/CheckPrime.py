import math


def check_prime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return "No"
    else:
        return "Yes"


print(check_prime(10))