n = int(input())
n_lst = sorted(list(map(int, input().split())))
print(n_lst[-1] - n_lst[0])