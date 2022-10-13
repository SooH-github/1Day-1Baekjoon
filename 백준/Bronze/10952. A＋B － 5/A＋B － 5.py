import sys

print_lst = []
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == b == 0:
        break
    print_lst.append(a + b)
    
for i in print_lst:
    print(i)