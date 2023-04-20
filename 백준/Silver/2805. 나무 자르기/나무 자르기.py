n, m = map(int, input().split())
n_lst = list(map(int, input().split()))
s, e = 1, max(n_lst)

while s <= e:
    c = (s + e) // 2
    
    x = 0
    for i in n_lst:
        if i >= c:
            x += i - c
    
    if x >= m:
        s = c + 1
    else:
        e = c - 1
        
print(e)