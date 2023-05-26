import sys

st_pw = {}
n, m = map(int, sys.stdin.readline().split())

for i in range(n):
    st, pw = sys.stdin.readline().split()
    st_pw[st] = pw

for i in range(m):
    print(st_pw[sys.stdin.readline().strip()])