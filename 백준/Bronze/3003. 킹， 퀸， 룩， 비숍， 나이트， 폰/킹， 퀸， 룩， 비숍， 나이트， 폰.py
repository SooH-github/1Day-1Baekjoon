chess_lst = [1, 1, 2, 2, 2, 8]
input_lst = list(map(int, input().split()))

print_lst = []
for x, y in zip(chess_lst, input_lst):
	print_lst.append(x - y)

print(' '.join(map(str, print_lst)))