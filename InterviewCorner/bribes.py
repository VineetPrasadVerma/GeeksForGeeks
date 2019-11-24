# # Complete the minimumBribes function below.
# def minimumBribes(q):
#     # counter = 0
#     # for idx, value in enumerate(q):
#     #     diff = value - (idx+1)
#     #
#     #     if diff > 2:
#     #         return 'Too chaotic'
#     #
#     #     if value > (idx+1):
#     #         counter += diff
#     #
#     # return counter
#     total_bribes = 0
#     for i in range(len(q)):
#         for j in range(i+1, len(q)):
#             counter = 0
#             if q[i] > q[j]:
#                 counter += 1
#             if counter > 2:
#                 print("Too Chaotic")
#                 break
#             else:
#                 total_bribes += counter
#     print(total_bribes)
#
#
# if __name__ == '__main__':
#     t = int(input())
#
#     for t_itr in range(t):
#         n = int(input())
#
#         q = list(map(int, input().rstrip().split()))
#
#         print(minimumBribes(q))

def minimumBribes(q):
    total_bribes = 0
    for i in range(len(q)):
        counter = 0
        for j in range(i+1, len(q)):
            if q[i] > q[j]:
                counter += 1
        if counter > 2:
            print("Too chaotic")
            break
        else:
            total_bribes += counter
    else:
        print(total_bribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
