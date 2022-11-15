print_lst = []
n = int(input())
for i in range(n):
    print_lst.append(input())

for i in range(n):
    print(f"{i + 1}. {print_lst[i]}")