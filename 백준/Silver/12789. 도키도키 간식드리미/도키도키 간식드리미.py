import sys

n = int(input())
line = list(map(int, sys.stdin.readline().split()))

stack = []
waiting = 1

for person in line:
    while stack and stack[-1] == waiting:
        stack.pop()
        waiting += 1
    
    if person == waiting:
        waiting += 1
    else:
        stack.append(person)

while stack and stack[-1] == waiting:
    stack.pop()
    waiting += 1

if not stack:
    print("Nice")
else:
    print("Sad")