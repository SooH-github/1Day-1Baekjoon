def d(n):
    return n + sum(list(map(int, str(n))))

num_lst = list(range(10000))
for i in range(10000):
    if d(i) < 10000:
        if d(i) in num_lst:
            del num_lst[num_lst.index(d(i))]

for i in num_lst:
    print(i)