test_cases = int(input())
for _ in range(test_cases):
    size = int(input())
    target = input()
    reverse_string = target[::-1]
    if target == reverse_string:
        print('Yes')
    else:
        print("No")
