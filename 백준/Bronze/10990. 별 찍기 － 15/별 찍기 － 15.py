n = int(input())
for i in range(1, n + 1):
    if i == 1:
        print(" " * (2 * n // 2 - 1) + "*")
    else:
        print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")