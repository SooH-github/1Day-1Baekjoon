import sys

n = int(sys.stdin.readline())
n_lst = list(map(int, sys.stdin.readline().split()))

x_lst = sorted(list(set(n_lst)))
x_dic = {x_lst[i] : i for i in range(len(x_lst))}
for i in n_lst:
    print(x_dic[i], end = ' ')