import sys

x_lst = []
y_lst = []
for i in range(int(sys.stdin.readline())) :
    x, y = map(int, sys.stdin.readline().split())
    x_lst.append(x)
    y_lst.append(y)
    
print((max(x_lst) - min(x_lst)) * (max(y_lst) - min(y_lst)))