m, n = map(int, input().split())
num_lst = []
for i in range(m, n + 1):
    if i != 1:
        if i == 2:
            num_lst.append(2)
            continue
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            num_lst.append(i)
                
for i in num_lst:
    print(i)