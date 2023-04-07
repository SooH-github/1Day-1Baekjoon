import sys

n, m = map(int, sys.stdin.readline().split())

poket = {}
for i in range(1, n + 1):
    x = sys.stdin.readline().rstrip()
    poket[i] = x
    poket[x] = i

for i in range(m):
    y = sys.stdin.readline().rstrip()
    if y.isdigit():
        print(poket[int(y)])
    else:
        print(poket[y])