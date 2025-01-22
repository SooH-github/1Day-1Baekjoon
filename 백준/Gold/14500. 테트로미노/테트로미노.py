def solve_tetromino(n, m, grid):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    max_sum = 0

    def dfs(x, y, depth, total):
        nonlocal max_sum
        if depth == 4:
            max_sum = max(max_sum, total)
            return
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, depth + 1, total + grid[nx][ny])
                visited[nx][ny] = False

    def check_t_shape(x, y):
        nonlocal max_sum
        for i in range(4):
            total = grid[x][y]
            for j in range(3):
                nx = x + dx[(i + j) % 4]
                ny = y + dy[(i + j) % 4]
                if not (0 <= nx < n and 0 <= ny < m):
                    break
                total += grid[nx][ny]
            else:
                max_sum = max(max_sum, total)

    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            visited[i][j] = True
            dfs(i, j, 1, grid[i][j])
            visited[i][j] = False
            check_t_shape(i, j)

    return max_sum


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
print(solve_tetromino(n, m, grid))