input_lst = list(input())
print_sum = 0

for i in range(len(input_lst)):
    if i == 0:
        print_sum += 10
    elif input_lst[i - 1] == input_lst[i]:
        print_sum += 5
    else:
        print_sum += 10

print(print_sum)