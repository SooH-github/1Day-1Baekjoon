import sys
from collections import deque

n_lst = deque([])
for i in range(int(sys.stdin.readline())):
    x = sys.stdin.readline().split()
    if x[0] == "push":
        n_lst.append(x[1])
    elif x[0] == "pop":
        if len(n_lst) == 0:
            print(-1)
        else:
            print(n_lst.popleft())
    elif x[0] == "size":
        print(len(n_lst))
    elif x[0] == "empty":
        if len(n_lst) == 0:
            print(1)
        else:
            print(0)
    elif x[0] == "front":
        if len(n_lst) == 0:
            print(-1)
        else:
            print(n_lst[0])
    elif x[0] == "back":
        if len(n_lst) == 0:
            print(-1)
        else:
            print(n_lst[-1])