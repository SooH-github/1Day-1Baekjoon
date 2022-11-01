n = int(input())
n_lst = list(map(int, input().split()))
count = 0
for i in n_lst:
    if i != 1:
        if i == 2:
            count += 1
            continue
        for j in range(2, i):
            if i % j == 0:
                break
            if j == i - 1:
                count += 1
print(count)