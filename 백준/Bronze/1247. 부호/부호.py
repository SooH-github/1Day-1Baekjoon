import sys

for i in range(3):
    n_lst = []
    for i in range(int(sys.stdin.readline())):
        n_lst.append(int(sys.stdin.readline()))
    
    if sum(n_lst) == 0:
        print(0)
    elif sum(n_lst) < 0:
        print("-")
    else:
        print("+")