import sys

n = int(sys.stdin.readline())
queue = []

for i in range(n):
    ment = sys.stdin.readline().split()

    if ment[0] == "push":
        queue.insert(0, ment[1])
        
    elif ment[0] == "pop":
        if len(queue) != 0:
            print(queue.pop())
        else:
            print(-1)
            
    elif ment[0] == "size":
        print(len(queue))

    elif ment[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif ment[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue) - 1])

    elif ment[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])