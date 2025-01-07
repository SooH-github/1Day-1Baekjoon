def z(n, r, c):
    if n == 0:
        return 0
    half = 2 ** (n - 1)
    x = half * half
    if r < half and c < half:
        return z(n - 1, r, c)
    elif r < half and c >= half:
        return x + z(n - 1, r, c - half)
    elif r >= half and c < half:
        return 2 * x + z(n - 1, r - half, c)
    else:
        return 3 * x + z(n - 1, r - half, c - half)

n, r, c = map(int, input().split())
print(z(n, r, c))