import sys

n, m = map(int, sys.stdin.readline().split())
n_lst = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
sum_n = [[0] * (n + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        sum_n[i][j] = sum_n[i][j - 1] + sum_n[i - 1][j] - sum_n[i - 1][j - 1] + n_lst[i - 1][j - 1]

for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(sum_n[x2][y2] - sum_n[x1 - 1][y2] - sum_n[x2][y1 - 1] + sum_n[x1 - 1][y1 - 1])