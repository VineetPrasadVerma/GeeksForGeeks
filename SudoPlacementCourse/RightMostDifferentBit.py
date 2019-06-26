test_cases = int(input())
for _ in range(test_cases):
    m, n = tuple(map(int, input().split()))
    m_binary_from = list('{0:0b}'.format(m))
    n_binary_from = list('{0:0b}'.format(n))
    len_m = len(m_binary_from)
    len_n = len(n_binary_from)
    if m == n:
        print(-1)
        break
    l = []
    trailing_zero_size = abs(len_m - len_n)
    for i in range(trailing_zero_size):
        l.append('0')
    less_size = min(len_m, len_n)
    if less_size == len_m:
        m_binary_from = l + m_binary_from
    else:
        n_binary_from = l + n_binary_from

    for i in range(len(m_binary_from) - 1, -1, -1):
        if m_binary_from[i] == n_binary_from[i]:
            pass
        else:
            print(len(m_binary_from) - i)
            break


