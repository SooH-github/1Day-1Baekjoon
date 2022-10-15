print_lst = []
for i in range(int(input())):
    input_lst = list(map(int, input().split()))
    average = sum(input_lst[1:]) / input_lst[0]
    count = 0
    for x in input_lst[1:]:
        if average < x:
            count += 1
    print_lst.append(f"{count / input_lst[0] * 100:.3f}%")
    
for i in print_lst:
    print(i)