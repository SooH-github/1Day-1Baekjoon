x, y, w, h = map(int, input().split())
n_lst = [x - 0, y - 0, w - x, h - y]
print(min(n_lst))