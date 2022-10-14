input_lst = []
for i in range(9):
    input_lst.append(int(input()))

print(max(input_lst))
print(input_lst.index(max(input_lst)) + 1)