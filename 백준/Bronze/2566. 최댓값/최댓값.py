print_max, x, y = 0, 0, 0
for i in range(9):
    n_lst = list(map(int, input().split()))
    if print_max < max(n_lst):
        print_max = max(n_lst)
        x = i
        y = n_lst.index(print_max)
        
print(print_max)
print(x + 1, y + 1)