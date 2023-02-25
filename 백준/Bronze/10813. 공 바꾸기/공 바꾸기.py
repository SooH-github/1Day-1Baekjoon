n, m = map(int, input().split())
n_lst = [str(i + 1) for i in range(n)]

for i in range(m):
    i, j = map(int, input().split())
    n_lst[i - 1], n_lst[j - 1] = n_lst[j - 1], n_lst[i - 1]

print(*n_lst)