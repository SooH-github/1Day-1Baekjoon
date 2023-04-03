n, b = map(int,input().split())
b_lst = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print_b = ""

while True:
    if n == 0:
        break   
    print_b += str(b_lst[n % b])
    n = n // b
    
print(print_b[::-1])