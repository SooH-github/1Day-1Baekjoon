n, m = map(int, input().split())
bsk = [0] * (n + 1)

for x in range(m):
    i, j, k = map(int, input().split())
    for u in range(i, j + 1):
        bsk[u] = k 

for i in range(1, n + 1):
    print(bsk[i], end = " ")