n_lst = []
for i in range(int(input())):
    a, b, c = map(int, input().split())
    
    if a == b == c:
        n_lst.append(10000 + a * 1000)
    elif a == b or a == c:
        n_lst.append(1000 + a * 100)
    elif b == c:
        n_lst.append(1000 + b * 100)
    else:
        n_lst.append(max(a, b, c) * 100)

print(max(n_lst))