n, m = map(int,input().split())
n_lst = []
for i in range(n):
    n_lst.append(input())

a, b = 0, 0
for i in range(n):
    if "X" not in n_lst[i]:
        a += 1
for j in range(m):
    if "X" not in [n_lst[i][j] for i in range(n)]:
        b += 1

print(max(a ,b))