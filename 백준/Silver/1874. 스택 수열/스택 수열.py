cnt = 1
x = True
n_lst = []
x_lst = []

N = int(input())
for i in range(N):
    num = int(input())
    while cnt <= num:
        n_lst.append(cnt)
        x_lst.append("+")
        cnt += 1

    if n_lst[-1] == num:
        n_lst.pop()
        x_lst.append("-")

    else:
        x = False
        break

if x == False:
    print("NO")
else:
    for i in x_lst:
        print(i)