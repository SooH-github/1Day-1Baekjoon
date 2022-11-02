n = int(input())
n_lst = []
x = 2

while n != 1:
    if n % x != 0:
        x += 1
    else:
        n //= x
        n_lst.append(x)
        
for i in n_lst:
    print(i)