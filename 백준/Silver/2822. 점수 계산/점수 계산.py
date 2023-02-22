score = []
for i in range(8):
    score.append(int(input()))
score_ = sorted(score)[::-1]

x = []
for i in range(5):
    x.append(score_[i])

total = 0
y = []
for i in x:
    total += i
    y.append(score.index(i))
print(total)

y_ = sorted(y)
for i in y_:
    print(i + 1, end=" ")