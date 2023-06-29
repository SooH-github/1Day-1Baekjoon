import sys

n_lst = [True for i in range(1000001)]
for i in range(2, 1001):
    if n_lst[i]:
        for j in range(i + i , 1000001, i):
            n_lst[j] = False

for i in range(int(input())):
    print_n = 0
    n = int(sys.stdin.readline())

    for j in range(2, n // 2 + 1):
        if n_lst[j] and n_lst[n - j]:
            print_n += 1
    print(print_n)