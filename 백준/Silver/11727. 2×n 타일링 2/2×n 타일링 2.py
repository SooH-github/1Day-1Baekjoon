n = int(input())
r = [0] * 1001

r[0] = 1
r[1] = 1

for i in range(2, n + 1):
    r[i] = r[i - 1] + 2 * r[i - 2]

print(r[n] % 10007)