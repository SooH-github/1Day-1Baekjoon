import sys

n, k = map(int,sys.stdin.readline().split())
n_lst = list(map(int, sys.stdin.readline().split()))

print_n = []
print_n.append(sum(n_lst[:k]))

for i in range(n - k):
    print_n.append(print_n[i] - n_lst[i] + n_lst[k + i])
        
print(max(print_n))