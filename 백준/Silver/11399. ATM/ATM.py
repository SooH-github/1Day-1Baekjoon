n = int(input())
n_lst = sorted(list(map(int, input().split())))
n_sum = 0

for i in range(n):
    for j in range(i + 1):
        n_sum += n_lst[j]
print(n_sum)