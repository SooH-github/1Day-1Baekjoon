import sys

n  = int(sys.stdin.readline())
deque = []

for i in range(n):
    ment = sys.stdin.readline().split()
    
    if ment[0] == "push_front":
        deque.insert(0, ment[1])
    
    elif ment[0] == "push_back":
        deque.append(ment[1])
    
    elif ment[0] == "pop_front": 
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(0))
            
    elif ment[0] == "pop_back": 
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(-1))
    
    elif ment[0] == "size":
        print(len(deque))
    
    elif ment[0] == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
            
    elif ment[0] == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
            
    elif ment[0] == "back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])