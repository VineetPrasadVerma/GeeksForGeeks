test_cases = int(input())
for _ in range(test_cases):
    binary_form = input()
    decimal_form = int(binary_form, 2)
    if decimal_form % 3 == 0:
        print(1)
    else:
        print(0)
