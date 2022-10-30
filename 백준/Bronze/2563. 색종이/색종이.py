white = [[0] * 101 for i in range(101)]
for i in range(int(input())):
    a, b = map(int, input().split())
    for x in range(10):
        for y in range(10):
            white[a + x][b + y] = 1

sum_num = 0
for i in white:
    sum_num += sum(i)
print(sum_num)