print_lst = []
for i in range(int(input())):
    input_lst = list(input())
    count = 0
    total = 0
    for x in input_lst:
        if x == "O":
            count += 1
            total += count
        else:
            count = 0
    print_lst.append(total)

for i in print_lst:
    print(i)