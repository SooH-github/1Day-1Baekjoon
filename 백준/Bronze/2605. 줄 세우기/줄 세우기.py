print_n = []
n = int(input())
n_lst = list(map(int, input().split()))

for i in range(n):
    print_n.insert(n_lst[i], i + 1)
    
print(*print_n[::-1])