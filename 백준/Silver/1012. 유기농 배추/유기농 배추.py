import sys
sys.setrecursionlimit(10**6)

def remove_connected(x, y, field, n, m):
    if x < 0 or x >= n or y < 0 or y >= m or field[x][y] == 0:
        return
    field[x][y] = 0
    remove_connected(x - 1, y, field, n, m)
    remove_connected(x + 1, y, field, n, m)
    remove_connected(x, y - 1, field, n, m)
    remove_connected(x, y + 1, field, n, m)

def count_worms(m, n, cabbages):
    field = [[0] * m for i in range(n)]
    for x, y in cabbages:
        field[y][x] = 1

    worms = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                remove_connected(i, j, field, n, m)
                worms += 1
    return worms

t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    cabbages = [tuple(map(int, input().split())) for i in range(k)]
    print(count_worms(m, n, cabbages))