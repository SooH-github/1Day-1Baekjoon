n = int(input())
test = list(map(int, input().split()))
total, score = 0, 0

for i in range(n):
    if test[i] == 0:
        score = 0
    else:
        score += 1
        total += score

print(total)