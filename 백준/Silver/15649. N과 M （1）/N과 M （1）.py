n, m = list(map(int, input().split()))
 
x_lst = []
def nnm():
    if len(x_lst)==m:
        print(" ".join(map(str, x_lst)))
        return
    for i in range(1, n + 1):
        if i not in x_lst:
            x_lst.append(i)
            nnm()
            x_lst.pop()
 
nnm()