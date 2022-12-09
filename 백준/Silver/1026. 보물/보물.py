n = int(input())
a = sorted(list(map(int, input().split())))
b = list(map(int, input().split()))

sum_n = 0
for i in a:
    sum_n += i * max(b)
    b.pop(b.index(max(b)))
    
print(sum_n)