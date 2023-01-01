import sys

m = int(sys.stdin.readline())
m_lst = set(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline())
n_lst = list(map(int, sys.stdin.readline().split()))

for i in n_lst:
    if i in m_lst:
        print(1, end = " ")
    else:
        print(0, end = " ")