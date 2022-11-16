import sys

n_list = [0] * 10001

for i in range(int(input())):
    n_list[int(sys.stdin.readline())] += 1
    
for i in range(10001):
    if n_list[i] != 0:
        for j in range(n_list[i]):
            print(i)