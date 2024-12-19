n = int(input())
lens = 4 * n - 3
star = [[" "] * lens for _ in range(lens)]

for level in range(n):
    start = 2 * level
    end = lens - 2 * level

    for i in range(start, end):
        star[start][i] = "*"
        star[end - 1][i] = "*"

    for i in range(start, end):
        star[i][start] = "*"
        star[i][end - 1] = "*"

for row in star:
    print("".join(row))
