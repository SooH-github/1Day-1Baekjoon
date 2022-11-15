import math

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a / c < b / d:
    day = l - b / d
else:
    day = l - a / c
print(math.floor(day))