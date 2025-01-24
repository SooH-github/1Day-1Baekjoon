import math

def find_year(M, N, x, y):
    lcm = (M * N) // math.gcd(M, N)
    while x <= lcm:
        if (x - 1) % N + 1 == y:
            return x
        x += M
    return -1

T = int(input())
results = []
for i in range(T):
    M, N, x, y = map(int, input().split())
    results.append(find_year(M, N, x, y))

for res in results:
    print(res)