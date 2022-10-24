n_lst = [x for x in range(1, 31)]
for i in range(28):
    n = int(input())
    n_lst.pop(n_lst.index(n))

for i in n_lst:
    print(i)