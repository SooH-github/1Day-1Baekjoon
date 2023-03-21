n_lst = sorted(list(map(int, input().split())))
abc = list(input())

for i in abc:
    if i == "A":
        print(n_lst[0], end=" ")
    elif i == "B":
        print(n_lst[1], end=" ")
    else:
        print(n_lst[2], end=" ")