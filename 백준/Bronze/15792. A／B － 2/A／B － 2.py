a, b = map(int, input().split())
r = (str(a // b) + ".")
a = (a % b) * 10
for i in range(1000):
    r += str(a // b)
    a = (a % b) * 10
    
print(r)