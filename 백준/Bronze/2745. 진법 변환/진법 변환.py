n, b = input().split()
b_lst = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = n[::-1]
print_n = 0

for i, x in enumerate(n):
    print_n += (int(b) ** i) * (b_lst.index(x))
print(print_n)