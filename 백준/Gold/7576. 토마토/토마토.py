from collections import deque

M, N = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            queue.append((i, j))

days = 0
while queue:
    for _ in range(len(queue)):
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:
                grid[nx][ny] = 1
                queue.append((nx, ny))
    if queue:
        days += 1

if any(0 in row for row in grid):
    print(-1)
else:
    print(days)