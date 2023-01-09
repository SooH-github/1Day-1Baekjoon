n_lst = []

for i in range(int(input())):
    x, y = map(int, input().split())
    n_lst.append([x, y])

for i in n_lst:
    rank = 1
    for j in n_lst:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")