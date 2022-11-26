p, k = map(int, input().split())
t = True
for i in range(2, k):
    if p % i == 0:
        print('BAD', i)
        t = False
        break
if t:
    print('GOOD')