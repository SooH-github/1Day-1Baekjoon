from collections import deque

def shortest_distance(grid):
    n, m = len(grid), len(grid[0])
    distances = [[-1] * m for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                queue.append((i, j))
                distances[i][j] = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and distances[nx][ny] == -1 and grid[nx][ny] == 1:
                distances[nx][ny] = distances[x][y] + 1
                queue.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                distances[i][j] = 0

    return distances

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

result = shortest_distance(grid)

for row in result:
    print(" ".join(map(str, row)))