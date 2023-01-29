day = 0
mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, input().split())
for i in range(x - 1):
    day += mon[i]

day = (day + y) % 7
print(week[day])