import sys
from math import gcd

n = int(sys.stdin.readline())
a = int(sys.stdin.readline())
n_lst = []

for i in range(n - 1):
    x = int(sys.stdin.readline())
    n_lst.append(x - a)
    a = x

y = n_lst[0]
for j in range(1, len(n_lst)):
    y = gcd(y, n_lst[j])

print_n = 0
for i in n_lst:
    print_n += i // y - 1
print(print_n)