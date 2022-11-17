n_lst = []
for i in range(5):
    n_lst.append(int(input()))
    
print(sum(n_lst) // 5)
print(sorted(n_lst)[2])