n = 1000 - int(input())
joi = [500, 100, 50, 10, 5, 1]
cnt = 0
for i in joi:
    cnt += n // i
    n %= i
print(cnt)