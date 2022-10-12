import sys

t = int(input())

print_lst = []
for i in range(t):
    print_lst.append(list(map(int, sys.stdin.readline().split())))

for i in range(len(print_lst)):
    print(f"Case #{i + 1}: {print_lst[i][0]} + {print_lst[i][1]} = {print_lst[i][0] + print_lst[i][1]}")