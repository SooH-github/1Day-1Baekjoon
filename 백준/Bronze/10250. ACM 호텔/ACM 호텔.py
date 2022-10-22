import sys, math

print_lst = []
for i in range(int(input())):
    h, w, n = map(int, sys.stdin.readline().split())
    if n % h == 0:
        print_lst.append(f"{h}{str(math.ceil(n / h)).zfill(2)}")
    else:
        print_lst.append(f"{n % h}{str(math.ceil(n / h)).zfill(2)}")

for i in print_lst:
    print(i)