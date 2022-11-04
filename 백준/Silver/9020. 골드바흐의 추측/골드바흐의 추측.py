import math

n_lst = []
all_lst = [x for x in range(10000)]
for i in all_lst:
    if i != 1:
        if i == 2:
            n_lst.append(2)
            continue
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            n_lst.append(i)

print_lst = []
for i in range(int(input())):
    n = int(input())
    x1, x2 = n // 2, n // 2
    
    while True:
        if x1 in n_lst and x2 in n_lst:
            print_lst.append(f"{x1} {x2}")
            break
        else:
            x1 -= 1
            x2 += 1
            
for i in print_lst:
    print(i)