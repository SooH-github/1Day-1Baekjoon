n = int(input())
n_lst = list(map(int, input().split()))        
pc = [0] * 101
p = 0

for i in n_lst:
    if pc[i] != 0:
        p += 1
    else:
        pc[i] += 1

print(p)