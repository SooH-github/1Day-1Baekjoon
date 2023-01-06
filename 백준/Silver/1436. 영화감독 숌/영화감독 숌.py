n = int(input())
th = 666
cnt = 0

while True:
    if "666" in str(th):
        cnt += 1
    if cnt == n:
        print(th)
        break
    th += 1