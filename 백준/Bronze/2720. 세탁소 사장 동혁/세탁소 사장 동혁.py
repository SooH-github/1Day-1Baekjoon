money = [25, 10, 5, 1]
coin = [0] * 4

for i in range(int(input())):
    c = int(input())

    for j in range(len(money)):
        coin[j] = c // money[j]
        c = c % money[j]

    print(' '.join(map(str, coin)))