l = int(input())
e_str = input()
print_n = 0

for i in range(l):
    print_n += (ord(e_str[i])-96) * (31 ** i)
    
print(print_n % 1234567891)