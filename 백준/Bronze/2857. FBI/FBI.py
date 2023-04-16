n_lst = []
for i in range(5):
    name = input()
    if "FBI" in name:
        n_lst.append(str(i + 1))

if n_lst == []:
    print("HE GOT AWAY!")
else:
    print(" ".join(n_lst))