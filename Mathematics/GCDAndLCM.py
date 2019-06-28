def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


t = int(input())
for _ in range(t):
    num_a, num_b = tuple(map(int, input().split()))
    gcd = gcd(num_a, num_b)
    lcm = (num_a * num_b) // gcd
    print(lcm, gcd)