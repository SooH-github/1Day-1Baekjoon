from collections import deque

n = int(input())
balloons = list(map(int, input().split()))

dq = deque((i + 1, balloons[i]) for i in range(n))
result = []

while dq:
    idx, move = dq.popleft()
    result.append(idx)
    if dq:
        if move > 0:
            dq.rotate(-(move - 1))
        else:
            dq.rotate(-move)

print(" ".join(map(str, result)))