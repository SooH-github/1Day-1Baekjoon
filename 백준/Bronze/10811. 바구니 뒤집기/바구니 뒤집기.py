import sys

n, m = map(int, sys.stdin.readline().split())
n_lst = [i + 1 for i in range(n)]

for x in range(m):
    i, j = map(int, sys.stdin.readline().split())
    n_lst[i - 1:j] = n_lst[i - 1:j][::-1]
    
print(*n_lst)