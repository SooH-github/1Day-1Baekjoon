def hansu(n):
    if int(n[0]) - int(n[1]) ==int(n[1]) - int(n[2]):
        return 1
    else:
        return 0

count = 0
n = int(input())
for i in range(1, n + 1):
    if i < 100:
        count += 1
    else:
        count += hansu(str(i))

print(count)