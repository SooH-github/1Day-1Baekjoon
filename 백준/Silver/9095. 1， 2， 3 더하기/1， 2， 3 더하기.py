import sys

n_lst = [0] * 11
n_lst[1] = 1
n_lst[2] = 2
n_lst[3] = 4

for i in range(4, 11):
    n_lst[i] = sum(n_lst[i - 3:i])

for i in range(int(sys.stdin.readline())):
    print(n_lst[int(sys.stdin.readline())])