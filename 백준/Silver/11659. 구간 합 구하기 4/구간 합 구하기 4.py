import sys

n, m = map(int, sys.stdin.readline().split())
n_lst = list(map(int, sys.stdin.readline().split()))

for i in range(n - 1):
    n_lst[i + 1] += n_lst[i]
n_lst = [0] + n_lst

for x in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(n_lst[j] - n_lst[i - 1])