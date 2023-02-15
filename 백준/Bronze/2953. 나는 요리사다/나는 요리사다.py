s_lst = []
for i in range(5):
    s_lst.append(sum(map(int, input().split())))

print(s_lst.index(max(s_lst)) + 1, max(s_lst))