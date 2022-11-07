n, m = map(int, input().split())
card_lst = list(map(int, input().split()))

max_num = 0
for i in range(n):
    for j in range(i + 1, n):
        for x in range(j + 1, n):
            if m < card_lst[i] + card_lst[j] + card_lst[x]:
                continue
            if max_num < card_lst[i] + card_lst[j] + card_lst[x]:
                max_num = card_lst[i] + card_lst[j] + card_lst[x]
print(max_num)