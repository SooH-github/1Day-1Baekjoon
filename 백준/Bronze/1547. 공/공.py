n_lst = [0,1,2,3]

for i in range(int(input())):
    x, y = map(int, input().split())
    n_lst[x], n_lst[y] = n_lst[y], n_lst[x]

print(n_lst.index(1))