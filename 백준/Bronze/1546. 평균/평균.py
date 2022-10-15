n = int(input())
input_lst = list(map(int, input().split()))

print(sum(input_lst) * 100 / max(input_lst) / n)