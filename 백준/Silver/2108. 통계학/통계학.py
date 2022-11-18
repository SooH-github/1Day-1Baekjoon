from collections import Counter
import sys

n_lst = []
for i in range(int(sys.stdin.readline())):
    n_lst.append(int(sys.stdin.readline()))
    
print(round(sum(n_lst) / len(n_lst)))
print(sorted(n_lst)[len(n_lst) // 2])
cnt = Counter(sorted(n_lst)).most_common(2)
if 1 < len(n_lst):
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(sorted(n_lst)[-1] - sorted(n_lst)[0])