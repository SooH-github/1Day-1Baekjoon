score_lst = []
for i in range(5):
    score = int(input())
    if score < 40:
        score_lst.append(40)
    else:
        score_lst.append(score)

print(sum(score_lst) // 5)