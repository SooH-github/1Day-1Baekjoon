n_lst = [0, 1, 2]
for i in range(3, 1001):
  n_lst.append(n_lst[i - 2] + n_lst[i - 1])

print(n_lst[int(input())] % 10007)