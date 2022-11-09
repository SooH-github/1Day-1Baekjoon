for i in range(int(input())):
    a = list(input())
    result = 0
    for i in a:
        if i == "(":
            result += 1
        elif i == ")":
            result -= 1
        if result < 0:
            print("NO")
            break
        
    if 0 < result:
        print("NO")
    elif result == 0:
        print("YES")