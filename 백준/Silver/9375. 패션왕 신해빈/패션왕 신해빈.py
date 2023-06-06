for i in range(int(input())):
    n = int(input())
    
    n_dic = {}
    for j in range(n):
        wear = list(input().split())
        if wear[1] in n_dic:
            n_dic[wear[1]].append(wear[0])
        else:
            n_dic[wear[1]] = [wear[0]]

    cnt = 1
    for j in n_dic:
        cnt *= (len(n_dic[j]) + 1)
    print(cnt - 1)