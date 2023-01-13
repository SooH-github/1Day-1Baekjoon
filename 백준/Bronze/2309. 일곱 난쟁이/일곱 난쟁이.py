n_lst = []

for i in range(9):
    n_lst.append(int(input()))

sum_n = sum(n_lst)
nan1 = 0
nan2 = 0

for i in range(8):
    for j in range(i + 1, 9):
        if sum_n - n_lst[i] - n_lst[j] == 100:
            nan1 = n_lst[i]
            nan2 = n_lst[j]
            
n_lst.remove(nan1)
n_lst.remove(nan2)

for i in sorted(n_lst):
    print(i)