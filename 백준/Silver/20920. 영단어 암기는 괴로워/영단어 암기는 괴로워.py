import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
w_lst = {}

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if len(word) < m:
        continue
    else:
        if word in w_lst:
            w_lst[word] += 1
        else:
            w_lst[word] = 1
w_lst = sorted(w_lst.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in w_lst:
    print(i[0])