n, k = map(int, input().split())
x_lst = list(map(int, input().split()))

print(sorted(x_lst)[::-1][k - 1])