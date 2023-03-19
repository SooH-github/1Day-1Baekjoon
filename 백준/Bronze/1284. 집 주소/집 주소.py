while True:
    n = input()
    if n == "0":
        break
        
    print_n = len(n) + 1
    for i in n:
        if i == "0":
            print_n += 4 
        elif i == "1":
            print_n += 2
        else:
            print_n += 3
            
    print(print_n)