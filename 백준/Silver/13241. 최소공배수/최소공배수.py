a, b = map(int, input().split())

def gcd(a, b):
    while b:
        x = b
        b = a % b
        a = x
    return a

print(a * b // gcd(a, b))