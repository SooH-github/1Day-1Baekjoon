h1, m1, s1 = map(int, input().split(":"))
h2, m2, s2 = map(int, input().split(":"))

t1 = h1 * 3600 + m1 * 60 + s1
t2 = h2 * 3600 + m2 * 60 + s2

if t2 < t1:
    t = t2 - t1 + 86400
else:
    t = t2 - t1

h = t // 3600
m = t // 60 % 60
s = t % 60

if h == m == s == 0:
    print("24:00:00")
else:
    print("%02d:%02d:%02d" % (h, m, s))