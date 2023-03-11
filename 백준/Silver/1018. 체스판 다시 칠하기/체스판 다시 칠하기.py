n, m = map(int, input().split())
chess = []
cnt = []

for i in range(n):
    chess.append(input())
    
for i in range(n - 7):
    for j in range(m - 7):
        x = 0
        y = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (b + a) % 2 == 0:
                    if chess[a][b] != "W":
                        x += 1  
                    if chess[a][b] != "B":
                        y += 1
                else :
                    if chess[a][b] != "B":
                        x += 1
                    if chess[a][b] != "W":
                        y += 1
        cnt.append(x)
        cnt.append(y)

print(min(cnt))