from collections import defaultdict

n = int(input())
m = int(input())

graph = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

stack = [1]
checked = set()

while stack:
    com = stack.pop()
    if com not in checked:
        checked.add(com)
        stack.extend(graph[com])

print(len(checked) - 1)
