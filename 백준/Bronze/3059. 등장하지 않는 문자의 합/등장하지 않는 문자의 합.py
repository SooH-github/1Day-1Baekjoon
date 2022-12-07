alpha = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for i in range(int(input())):
    input_lst = set(input())
    x_lst = alpha - input_lst
    
    print_n = 0
    for j in x_lst:
        print_n += ord(j)
    print(print_n)