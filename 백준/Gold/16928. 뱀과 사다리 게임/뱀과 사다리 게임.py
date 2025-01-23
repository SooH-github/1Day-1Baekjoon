from collections import deque

def bfs():
    visit = [False] * 101
    queue = deque([(1, 0)])
    visit[1] = True

    while queue:
        now, move = queue.popleft()
        if now == 100:
            return move

        for dice in range(1, 7):
            next = now + dice
            if next > 100:
                continue
            next = board.get(next, next)
            if not visit[next]:
                visit[next] = True
                queue.append((next, move + 1))

n, m = map(int, input().split())
board = {}

for i in range(n + m):
    start, end = map(int, input().split())
    board[start] = end

print(bfs())