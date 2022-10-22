print_lst = []
for i in range(int(input())):
    k = int(input())
    n = int(input())
    f0_lst = [x for x in range(1, n + 1)]
    for i in range(k):
        for j in range(1, n):
            f0_lst[j] += f0_lst[j - 1]
    print_lst.append(f0_lst[-1])

for i in print_lst:
    print(i)