alphabet_lst = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
print_time = 0

s = input()
for i in s:
    for j in alphabet_lst:
        if i in j:
            print_time += alphabet_lst.index(j) + 3
print(print_time)