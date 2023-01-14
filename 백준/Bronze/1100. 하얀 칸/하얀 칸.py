c_lst = []
for i in range(8):
    c_lst.append(list(map(str, list(input()))))

print_n = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            if c_lst[i][j] == "F":
                print_n += 1
print(print_n)