n = int(input())
n_lst = list(map(int, input().split()))
n_dic = {}
for i in n_lst:
    if i in n_dic:
        n_dic[i] += 1
    else:
        n_dic[i] = 1

m = int(input())
m_lst = list(map(int, input().split()))
for i in m_lst:
    if i in n_dic:
        print(n_dic[i], end = " ")
    else:
        print(0, end = " ")