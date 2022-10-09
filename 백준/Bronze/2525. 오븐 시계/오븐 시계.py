h, m = map(int, input().split())
plus_m = int(input())

if 59 < m + plus_m:
    h += (m + plus_m) // 60
    if 23 < h:
        h %= 24
    m = (m + plus_m) % 60
else:
    m += plus_m

print(h, m)