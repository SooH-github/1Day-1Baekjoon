m = int(input())
n = int(input())

n_lst = []
i = 1
while i ** 2 <= n:
    if m <= i ** 2 <= n:
        n_lst.append(i ** 2)
    i += 1
    
if n_lst == []:
    print(-1)
else:
    print(sum(n_lst))
    print(n_lst[0])