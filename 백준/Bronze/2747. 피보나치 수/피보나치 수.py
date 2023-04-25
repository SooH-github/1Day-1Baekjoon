f1, f2 = 0, 1
f = [0, 1]

while True:
    f3 = f1 + f2
    if 45 < len(f):
        break
    f.append(f3)
    f1, f2 = f2, f3

print(f[int(input())])