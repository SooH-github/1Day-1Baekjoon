x = int(input())
n = int(input())
total_lst = []

for i in range(n):
    a, b = map(int, input().split())
    total_lst.append(a * b)

if sum(total_lst) == x:
    print("Yes")
else:
    print("No")