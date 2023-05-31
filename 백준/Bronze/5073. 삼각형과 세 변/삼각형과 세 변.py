while True:
    n_lst = sorted(list(map(int, input().split())))
    
    if n_lst[0] == n_lst[1] == n_lst[2] == 0:
        break
    
    if n_lst[0] + n_lst[1] <= n_lst[2]:
        print("Invalid")
    elif n_lst[0] == n_lst[1] == n_lst[2]:
        print("Equilateral")
    elif n_lst[0] == n_lst[1] or n_lst[1] == n_lst[2] or n_lst[2] == n_lst[0]:
        print("Isosceles")
    else:
        print("Scalene")