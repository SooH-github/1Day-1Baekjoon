while True:
    n = int(input())
    if n == -1:
        break

    n_lst = []
    for i in range(1, n):
        if n % i == 0:
            n_lst.append(i)
    
    if sum(n_lst) == n:
        print(n, " = ", " + ".join(str(i) for i in n_lst), sep = "")
    else:
        print(f"{n} is NOT perfect.")