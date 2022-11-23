a, b = map(int, input().split())
n_list = []
for i in range(1, b + 1):
    for j in range(i):
        n_list.append(i)

sum_list = n_list[a - 1:b]
print(sum(sum_list))