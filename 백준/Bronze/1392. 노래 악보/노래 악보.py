n, q = map(int, input().split())
n_lst = [int(input()) for i in range(n)]
for _ in range(q):
    s = int(input())
    for i in range(n):
        if s < sum(n_lst[:i + 1]):
            print(i + 1)
            break