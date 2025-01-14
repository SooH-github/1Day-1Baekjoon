def count_friends(n, m, campus):
    cnt = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(n):
        for j in range(m):
            if campus[i][j] == 'I':
                stack = [(i, j)]
                campus[i][j] = 'V'

                while stack:
                    x, y = stack.pop()

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < n and 0 <= ny < m and campus[nx][ny] != 'X' and campus[nx][ny] != 'V':
                            if campus[nx][ny] == 'P':
                                cnt += 1
                            campus[nx][ny] = 'V'
                            stack.append((nx, ny))

    return cnt if cnt > 0 else "TT"

n, m = map(int, input().split())
campus = [list(input().strip()) for _ in range(n)]
print(count_friends(n, m, campus))