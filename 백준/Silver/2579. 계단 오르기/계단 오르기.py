x = int(input())
n = [0 for i in range(301)]
n_lst = [0 for i in range(301)]

for i in range(x):
    n[i] = int(input())
n_lst[0] = n[0]
n_lst[1] = n[0] + n[1]
n_lst[2] = max(n[1] + n[2], n[0] + n[2])

for i in range(3, x):
    n_lst[i] = max(n_lst[i - 3] + n[i - 1] + n[i], n_lst[i - 2] + n[i])
print(n_lst[x - 1])