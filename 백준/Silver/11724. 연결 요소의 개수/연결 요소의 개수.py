import sys
sys.setrecursionlimit(1000000)

def find(x):
    if lst[x] != x:
        lst[x] = find(lst[x])
    return lst[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            lst[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            lst[root_x] = root_y
        else:
            lst[root_y] = root_x
            rank[root_x] += 1

n, m = map(int, sys.stdin.readline().split())
lst = list(range(n + 1))
rank = [0] * (n + 1)

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    union(u, v)

st = set(find(i) for i in range(1, n + 1))
print(len(st))