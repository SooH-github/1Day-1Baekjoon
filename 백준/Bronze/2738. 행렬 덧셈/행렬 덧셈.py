n, m = map(int, input().split())
a, b = [], []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    b.append(list(map(int, input().split())))
for x in range(n):
    for y in range(m):
        print(a[x][y] + b[x][y], end = " ")
    print()