count = 0
n = int(input())
while 0 <= n:
    if n % 5 == 0:
        count += n // 5
        print(count)
        break
    n -= 3
    count += 1
else:
    print("-1")