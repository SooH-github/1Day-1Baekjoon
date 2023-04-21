x, y = map(int, input().split())
seven25 = x * 1000 / y

for i in range(int(input())):
    a, b = map(int, input().split())
    seven25 = min(seven25, a * 1000 / b)
print(round(seven25, 2))