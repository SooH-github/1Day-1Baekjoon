import sys
n_lst = [i + 1 for i in range(20)]

for i in range(10):
    m, n = map(int, sys.stdin.readline().split())
    a = n_lst[:m - 1]
    b = n_lst[m - 1:n][::-1]
    c = n_lst[n:]
    n_lst = a + b + c
    
for i in n_lst:
    print(i, end = " ")