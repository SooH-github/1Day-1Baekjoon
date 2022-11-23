n_lst = []
for i in range(7):
    n = int(input())
    if n % 2 != 0:
        n_lst.append(n)
        
if n_lst:
    print(sum(n_lst))
    print(min(n_lst))
else:
    print(-1)