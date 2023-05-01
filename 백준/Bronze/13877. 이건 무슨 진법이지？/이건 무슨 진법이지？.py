for i in range(int(input())):
    x, n = input().split()
    if max(list(n)) < "8":
        o = int(n, 8)
    else:
        o = 0
    
    print(f"{int(x)} {int(o)} {int(n)} {int(n, 16)}")