n = int(input())
for i in range(1, n):
    print("*" * i + " " * (n * 2 - i * 2) + "*" * i)
for i in range(n, 0, -1):
    print("*" * i + " " * (n * 2 - i * 2) + "*" * i)