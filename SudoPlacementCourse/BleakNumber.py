def count_set_bits(binary_form, n):
    return binary_form.count('1')


test_cases = int(input())
for _ in range(test_cases):
    num = int(input())
    binary_form = format(num, '0b')
    for i in range(1, len(binary_form)):
        if i + count_set_bits(binary_form, i) == num:
            print(0)
            break
    else:
        print(1)



