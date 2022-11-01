m = int(input())
n = int(input())
num_lst = []
for i in range(m, n + 1):
    if i != 1:
        if i == 2:
            num_lst.append(2)
            continue
        for j in range(2, i):
            if i % j == 0:
                break
            if j == i - 1:
                num_lst.append(i)
                
if num_lst == []:
    print(-1)
else:
    print(sum(num_lst))
    print(num_lst[0])