from collections import deque

def min_steps(start, target):
    if start >= target:
        return start - target
    max_limit = 100000
    visited = [False] * (max_limit + 1)
    queue = deque([(start, 0)])

    while queue:
        current, steps = queue.popleft()
        if current == target:
            return steps
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos <= max_limit and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, steps + 1))

start, target = map(int, input().split())
result = min_steps(start, target)
print(result)