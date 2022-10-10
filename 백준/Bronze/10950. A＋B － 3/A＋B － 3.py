t = int(input())
print_lst = []

for i in range(t):
    a, b = map(int, input().split())
    print_lst.append(a + b)
    
for num in print_lst:
    print(num)