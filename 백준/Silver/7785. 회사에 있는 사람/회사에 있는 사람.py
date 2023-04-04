import sys

n = int(sys.stdin.readline())
n_lst = {}

for i in range(n):
    a, b = map(str, sys.stdin.readline().split())

    if b == "enter":
        n_lst[a] = b
    else:
        del n_lst[a]

n_lst = sorted(n_lst.keys())[::-1]

for i in n_lst:
    print(i)