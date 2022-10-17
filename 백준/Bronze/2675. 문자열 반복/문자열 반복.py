print_lst = []
t = int(input())
for i in range(t):
    r, s = input().split()
    p = ""
    for j in s:
        p += j * int(r)
    print_lst.append(p)

for i in print_lst:
    print(i)