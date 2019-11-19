import math
arr = [7, 4, 3, 2]
even_count = 0
odd_count = 0
for i in arr:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Odd Pairs :-", even_count * odd_count)

temp = int((math.factorial(even_count))/math.factorial(2) * math.factorial(even_count - 2))
print("Even Pairs :-", temp + int((math.factorial(odd_count))/math.factorial(2) * math.factorial(odd_count - 2)))