l, p = map(int, input().split())
n_lst = list(map(int, input().split()))

n_print = []
for n in n_lst:
    n_print.append(n - l * p)

print(" ".join(map(str, n_print)))