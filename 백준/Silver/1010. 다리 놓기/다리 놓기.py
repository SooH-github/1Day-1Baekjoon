import math

for i in range(int(input())):
    n, m = map(int, input().split())
    b = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(b)