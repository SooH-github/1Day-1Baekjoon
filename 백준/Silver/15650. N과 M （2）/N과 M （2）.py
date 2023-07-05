n, m = list(map(int, input().split()))

x_lst = []
def nnm(s):
    if len(x_lst) == m:
        print(' '.join(map(str, x_lst)))
        return
    
    for i in range(s, n + 1):
        if i not in x_lst:
            x_lst.append(i)
            nnm(i + 1)
            x_lst.pop()

nnm(1)