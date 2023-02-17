from math import factorial
n, k = map(int, input().split())
x = factorial(n) // (factorial(k) * factorial(n - k))
print(x)