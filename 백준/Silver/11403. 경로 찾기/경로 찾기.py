n = int(input())
graph = []
for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)


for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1
                
for g in graph:
    print(*g)