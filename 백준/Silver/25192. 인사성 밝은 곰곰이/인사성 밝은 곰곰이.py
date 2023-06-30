n_dic = {}
cnt = 0

for i in range(int(input())):
    n = input()

    if n =="ENTER":
        for key, value in n_dic.items():
            if value == 1:
                cnt += 1
        n_dic = {}
    else:
        if n not in n_dic:
            n_dic[n] = 1

for key, value in n_dic.items():
    if value == 1:
        cnt += 1

print(cnt)