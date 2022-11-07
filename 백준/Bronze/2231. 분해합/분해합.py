n = int(input())
for i in range(1, n + 1):
    if i == n:
        print(0)
        
    x = sum(list(map(int, str(i))))
    if i + x == n:
        print(i)
        break