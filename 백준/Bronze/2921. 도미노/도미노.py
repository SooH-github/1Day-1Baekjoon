n = int(input())

n_lst = []
for x in range(0, n + 1):
    for y in range(x, n + 1):
        n_lst.append(x + y)
print(sum(n_lst))