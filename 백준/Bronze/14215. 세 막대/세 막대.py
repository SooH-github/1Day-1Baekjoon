lst = sorted(list(map(int, input().split())))
if lst[2] < lst[0] + lst[1]:
    print(sum(lst))
else:
    print((lst[0] + lst[1]) * 2 - 1)