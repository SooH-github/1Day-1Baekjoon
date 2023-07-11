a_lst = list(map(int, input().split(" ")))
b_lst = list(map(int, input().split(" ")))

a_cnt = 0
b_cnt = 0

for i in range(10):
    if b_lst[i] < a_lst[i]:
        a_cnt += 1
    elif a_lst[i] < b_lst[i]:
        b_cnt += 1

if b_cnt < a_cnt:
    print("A")
elif a_cnt < b_cnt:
    print("B")
else:
    print("D")