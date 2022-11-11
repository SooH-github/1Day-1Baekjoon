from collections import deque

n = int(input())
n_lst = deque([i for i in range(1, n + 1)])

while True:
    if len(n_lst) < 2:
        break
    n_lst.popleft()
    x = n_lst.popleft()
    n_lst.append(x)
    
print(n_lst[0])