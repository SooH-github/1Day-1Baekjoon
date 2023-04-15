from math import pi

i = 0
while True:
    i += 1
    d, n, t = map(float, input().split())
    if n == 0:
        break
    miles = d / 63360 * pi * n
    mph = miles / t * 3600
    print("Trip #%d: %.2f %.2f" % (i, miles, mph))