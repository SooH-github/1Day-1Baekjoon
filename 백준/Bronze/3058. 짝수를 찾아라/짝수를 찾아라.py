for i in range(int(input())):
    n_lst = list(map(int, input().split()))
    j_lst = []
    for i in n_lst:
        if i % 2 == 0:
            j_lst.append(i)
    print(f"{sum(j_lst)} {min(j_lst)}")