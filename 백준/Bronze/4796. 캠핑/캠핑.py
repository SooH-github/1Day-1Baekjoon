case = 0

while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    
    case += 1
    day = (v // p) * l
    day += min((v % p), l)
    print(f"Case {case}: {day}")