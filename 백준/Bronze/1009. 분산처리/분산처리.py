import sys

for i in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    n_a = a % 10
    
    if n_a == 0:
        print(10)
    elif n_a in [1, 5, 6]:
        print(n_a)
    elif n_a in [4, 9]:
        n_b = b % 2
        
        if n_b == 0:
            print(n_a * n_a % 10)
        else:
            print(n_a)
    
    else:
        n_b = b % 4
        
        if n_b == 0:
            print(n_a ** 4 % 10)
        else:
            print(n_a ** n_b % 10)