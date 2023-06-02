n = int(input())
n_lst = list(map(int, input().split()))

sum_n = [n_lst[0]]
for i in range(len(n_lst) - 1):
    sum_n.append(max(sum_n[i] + n_lst[i + 1], n_lst[i + 1]))
    
print(max(sum_n))