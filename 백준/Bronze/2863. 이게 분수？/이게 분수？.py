a, b = map(int, input().split())
c, d = map(int, input().split())

n_lst = [a / c + b / d, c / d + a / b, d / b + c / a, b / a + d / c]
print(n_lst.index(max(n_lst)))