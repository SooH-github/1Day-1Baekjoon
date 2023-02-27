n, m = map(int, input().split())
n_lst = [i + 1 for i in range(n)]

for x in range(m):
    i, j, k = map(int, input().split())
    n_lst[i - 1:j] = n_lst[k - 1:j] + n_lst[i - 1:k - 1]
    
print(*n_lst)