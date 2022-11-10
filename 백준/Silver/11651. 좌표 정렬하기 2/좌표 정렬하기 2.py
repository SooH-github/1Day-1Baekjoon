print_lst = []
for i in range(int(input())):
    x, y = map(int, input().split())
    print_lst.append([y, x])

print_lst.sort()
for y, x in print_lst:
    print(x, y)