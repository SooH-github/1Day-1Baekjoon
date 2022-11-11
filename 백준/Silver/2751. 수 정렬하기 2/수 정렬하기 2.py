import sys

n_lst = []
for i in range(int(input())):
    n_lst.append(int(sys.stdin.readline()))
    
for i in sorted(n_lst):
    print(i)