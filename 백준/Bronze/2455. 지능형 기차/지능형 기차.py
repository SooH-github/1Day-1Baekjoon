n_lst = []
n = 0

for i in range(4):
    a, b = map(int, input().split())
    n += b
    n -= a
    n_lst.append(n)

print(max(n_lst))