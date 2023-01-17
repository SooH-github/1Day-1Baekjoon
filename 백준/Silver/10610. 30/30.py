n = sorted(list(input()))[::-1]
sum_n = 0
for i in n:
    sum_n += int(i)
if sum_n % 3 != 0 or "0" not in n:
    print(-1)
else:
    print("".join(n))