n_lst = list(map(int, input().split()))
n = min(n_lst)

while True:
    cnt = 0
    
    for i in range(5):
        if n % n_lst[i] == 0:
            cnt += 1
            
    if cnt > 2:
        print(n)
        break
    
    n += 1