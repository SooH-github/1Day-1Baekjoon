x_lst = []
for i in range(int(input())):
    x_lst.append(input().split())
x_lst.sort(key = lambda x : int(x[0]))

for i in x_lst:
    print(i[0], i[1])