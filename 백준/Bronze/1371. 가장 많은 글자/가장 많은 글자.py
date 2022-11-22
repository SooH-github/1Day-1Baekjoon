import sys

alpha = "abcdefghijklmnopqrstuvwxyz"
cnt_lst = []
input_ = sys.stdin.read()
for i in alpha:
    cnt_lst.append(input_.count(i))

n_max = max(cnt_lst)
for i in range(len(cnt_lst)):
    if n_max == cnt_lst[i]:
        print(chr(i + 97), end = "")