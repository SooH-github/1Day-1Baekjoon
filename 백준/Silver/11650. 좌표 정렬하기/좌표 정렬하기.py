print_lst = []
for i in range(int(input())):
    x, y = map(int, input().split())
    print_lst.append([x, y])

print_lst.sort()
for x, y in print_lst:
    print(x, y)