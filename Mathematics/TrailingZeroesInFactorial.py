import math
t = int(input())
for _ in range(t):
    number = int(input())
    fact = str(math.factorial(number))
    print(len(fact) - len(fact.rstrip('0')))
