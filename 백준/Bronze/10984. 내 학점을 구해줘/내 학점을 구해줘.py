for i in range(int(input())):
    n = int(input())
    total_c = 0
    total_g = 0
    
    for j in range(n):
        c, g = map(float, input().split())
        total_c += c
        total_g += c * g
        
    total_x = total_g / total_c
    print(int(total_c), "%.1f" % total_x)