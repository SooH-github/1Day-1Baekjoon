n, m, k = map(int, input().split())

cnt = 0
while k <= n + m and 0 <= n and 0 <= m:
    n -= 2
    m -= 1
    cnt += 1
    
print(cnt - 1)