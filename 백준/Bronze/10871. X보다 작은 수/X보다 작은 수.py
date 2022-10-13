n, x = map(int, input().split())
a_lst = list(map(int, input().split()))

print_lst = []
for i in range(n):
    if a_lst[i] < x:
        print_lst.append(a_lst[i])

print(" ".join(map(str, print_lst)))