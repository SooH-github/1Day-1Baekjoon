import math, sys

n_lst = []
all_lst = [x for x in range(123457 * 2)]
for i in all_lst:
        if i != 1:
            if i == 2:
                n_lst.append(2)
                continue
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    break
            else:
                n_lst.append(i)

print_lst = []
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    count = 0
    for i in n_lst:
        if n < i <= n * 2:
            count += 1
        if n * 2 < i:
            print_lst.append(count)
            break

for i in print_lst:
    print(i)