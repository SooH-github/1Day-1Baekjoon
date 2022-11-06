print_lst = []
while True:
    n_lst = sorted(list(map(int, input().split())))
    a, b, c = n_lst[0], n_lst[1], n_lst[2]
    if a == b == c == 0:
        break
    if a ** 2 + b ** 2 == c ** 2:
        print_lst.append("right")
    else:
        print_lst.append("wrong")
        
for i in print_lst:
    print(i)