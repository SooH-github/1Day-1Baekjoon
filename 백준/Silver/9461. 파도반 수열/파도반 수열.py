P = [0, 1, 1, 1]
for i in range(4, 101):
    P.append(P[i - 3] + P[i - 2])

x = int(input())
for i in range(x):
    n = int(input())
    print(P[n])