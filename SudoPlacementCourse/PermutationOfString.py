import itertools
test_cases = int(input())
for _ in range(test_cases):
    target = input()
    sorted_target = sorted(target)
    ans_list = list(itertools.permutations(sorted_target, len(target)))
    for elements in ans_list:
        for i in elements:
            print("".join(i), end="")
        print(" ", end="")
    print()
