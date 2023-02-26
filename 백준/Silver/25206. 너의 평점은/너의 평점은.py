s_dic = {"A+" : 4.5, "A0" : 4.0, "B+" : 3.5, "B0" : 3.0, "C+" : 2.5, "C0" : 2.0, "D+" : 1.5, "D0" : 1.0, "F" : 0.0}
xs = 0
sum_x = 0

for i in range(20):
    n, x, s = input().split()
    if s == "P":
        continue
    xs += float(x) * s_dic[s]
    sum_x += float(x)

print(round(xs / sum_x, 6))