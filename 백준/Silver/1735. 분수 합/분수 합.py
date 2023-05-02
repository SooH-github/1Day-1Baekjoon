def cal(x, y):
    while x % y != 0:
        n = x % y
        x = y
        y = n
    return y
    
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

y = cal(a1 * b2 + b1 * a2, b1 * b2)

print((a1 * b2 + b1 * a2) // y, (b1 * b2) // y)