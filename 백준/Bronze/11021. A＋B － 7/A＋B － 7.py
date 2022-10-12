import sys

t = int(input())

print_lst = []
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print_lst.append(a + b)

for i in range(len(print_lst)):
    print(f"Case #{i + 1}: {print_lst[i]}")