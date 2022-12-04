n = ""
while True:
    try:
        n += input()
    except EOFError:
        break
n = n.replace("/n", "").replace(" ", "")
print(sum(list(map(int, n.split(",")))))