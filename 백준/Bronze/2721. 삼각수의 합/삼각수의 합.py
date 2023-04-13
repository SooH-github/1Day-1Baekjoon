for i in range(int(input())):
    n = int(input())
    print_n = sum(k * sum(range(k + 2)) for k in range(1, n + 1))
    print(print_n)