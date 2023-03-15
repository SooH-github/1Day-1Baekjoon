n = int(input())
r = list(map(int, input().split()))
c = list(map(int, input().split()))

min_c = 0
x = c[0]
for i in range(n - 1):
    if c[i] < x:
        x = c[i]
    min_c += x * r[i]

print(min_c)