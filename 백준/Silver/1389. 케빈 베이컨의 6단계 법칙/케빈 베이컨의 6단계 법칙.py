n, m = map(int, input().split())
graph = [[float("inf")] * (n + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

print(min(range(1, n + 1), key=lambda x: sum(graph[x][1:])))