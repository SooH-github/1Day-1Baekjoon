for i in range(3):
    y_lst = input()
    y_cnt = y_lst.count("0")
    
    if y_cnt == 1:
        print("A")
    elif y_cnt == 2:
        print("B")
    elif y_cnt == 3:
        print("C")
    elif y_cnt == 4:
        print("D")
    else:
        print("E")