x = int(input())
n_lst = [0] * 1000001
for i in range(2, x + 1):
    n_lst[i] = n_lst[i - 1] + 1
    
    if i % 2 == 0:
        n_lst[i] = min(n_lst[i], n_lst[i // 2] + 1)
    if i % 3 == 0:
        n_lst[i] = min(n_lst[i], n_lst[i // 3] + 1)

print(n_lst[x])