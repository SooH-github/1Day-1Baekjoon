from collections import deque
n, k = map(int, input().split())
deque_ = deque([])

for i in range(1, n + 1):
    deque_.append(i)
print("<", end = "")
while deque_:
    for i in range(k - 1):
        deque_.append(deque_[0])
        deque_.popleft()
    print(deque_.popleft(), end = "")
    if deque_:
        print(", ", end = "")
print(">")