import sys

n = int(input())
input_lst = sorted(list(map(int, sys.stdin.readline().split())))

print(input_lst[0], input_lst[-1])