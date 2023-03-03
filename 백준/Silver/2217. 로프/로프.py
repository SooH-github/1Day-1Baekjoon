n = int(input())
n_lst = []
for i in range(n):
    n_lst.append(int(input()))

print_n = []
for i in sorted(n_lst):
    print_n.append(i * n)
    n -= 1
    
print(max(print_n))