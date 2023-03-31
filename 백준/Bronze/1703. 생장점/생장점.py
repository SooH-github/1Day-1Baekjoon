while True:
    n_lst = list(map(int, input().split()))
    
    if n_lst == [0]:
        break
    
    n = 1
    for i in range(n_lst[0]):
        x = n_lst[2 * i + 1]
        a = n_lst[2 * i + 2]
        n = n * x - a
        
    print(n)