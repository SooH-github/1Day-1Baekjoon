n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())
t_pack = 0

for i in size:
    if i == 0:
        continue
    elif i <= t:
        t_pack += 1
    elif i % t == 0:
        t_pack += i // t
    else:
        t_pack += i // t + 1

p_pack = n // p
pen = n % p

print(t_pack)
print(f'{p_pack} {pen}')