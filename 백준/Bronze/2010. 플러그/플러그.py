import sys

n_sum = 1
n = int(sys.stdin.readline())

for i in range(n):
    n_sum += int(sys.stdin.readline())

print(n_sum - n)