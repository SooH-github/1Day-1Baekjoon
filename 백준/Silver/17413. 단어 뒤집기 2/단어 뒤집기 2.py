s = input()
x = ""
ans = ""

for i in s:
    if i == " ":
        if "<" not in x:
            ans += x[::-1] + i
            x = ""
        else:
            x += i
    elif i == "<":
        ans += x[::-1]
        x = ""
        x += i
    elif i == ">":
        ans += x + i
        x = ""
    else:
        x += i

ans += x[::-1]

print(ans)