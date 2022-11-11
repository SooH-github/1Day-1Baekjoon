import sys

n_lst = []
for i in range(int(input())):
    x = sys.stdin.readline().split()
    
    if x[0] == "push":
        n_lst.append(x[1])
    elif x[0] == "pop":
        if n_lst == []:
            print(-1)
        else:
            print(n_lst.pop())
    elif x[0] == "size":
        print(len(n_lst))
    elif x[0] == "empty":
        if n_lst == []:
            print(1)
        else:
            print(0)
    else:
        if n_lst == []:
            print(-1)
        else:
            print(n_lst[-1])