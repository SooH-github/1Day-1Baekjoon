def divide(x, y, size):
    color = paper[x][y]
    same_color = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                same_color = False
                break
        if not same_color:
            break

    if same_color:
        if color == 0:
            return (1, 0)
        else:
            return (0, 1)
    
    half = size // 2
    results = [
        divide(x, y, half),
        divide(x, y + half, half),
        divide(x + half, y, half),
        divide(x + half, y + half, half),
    ]
    
    white = sum(r[0] for r in results)
    blue = sum(r[1] for r in results)
    return white, blue

n = int(input())
paper = [list(map(int, input().split())) for i in range(n)]
cnt_white, cnt_blue = divide(0, 0, n)

print(cnt_white)
print(cnt_blue)