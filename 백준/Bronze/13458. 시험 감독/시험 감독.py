n = int(input())
a_lst = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = n
for a in a_lst:
    a -= b
    if 0 < a:
        if a % c:
            cnt += (a // c) + 1
        else:
            cnt += (a // c)

print(cnt)