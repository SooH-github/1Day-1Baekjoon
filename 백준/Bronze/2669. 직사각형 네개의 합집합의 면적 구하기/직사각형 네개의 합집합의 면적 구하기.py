n_lst = [[0 for i in range(101)] for i in range(101)]

for x in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            n_lst[i][j] = 1

print_n = 0
for i in range(1, 101):
    for j in range(1, 101):
        if n_lst[i][j]:
            print_n += 1
            
print(print_n)