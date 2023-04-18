import sys

while True:
    string = sys.stdin.readline().rstrip()
    stack = list()

    if string == ".":
        break

    for mark in string:
        if mark == "(":
            stack.append(mark)
        elif mark == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(mark)
                break
            
        elif mark == "[":
            stack.append(mark)
        elif mark == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(mark)
                break
    if stack:
        print("no")
    else:
        print("yes")