import sys
k, n = map(int, sys.stdin.readline().split())
n_lst = [int(sys.stdin.readline()) for i in range(k)]
s, e = 1, max(n_lst)

while s <= e:
    m = (s + e) // 2
    l = 0
    for i in n_lst:
        l += i // m
        
    if l >= n:
        s = m + 1
    else:
        e = m - 1
print(e)