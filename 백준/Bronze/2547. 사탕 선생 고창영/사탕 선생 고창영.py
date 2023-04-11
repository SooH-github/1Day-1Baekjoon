for i in range(int(input())):
    enter = input()
    n = int(input())
    n_lst = [int(input()) for i in range(n)]
    
    if sum(n_lst) % n == 0:
        print("YES")
    else:
        print("NO")