import sys

def solve(num):
  if num - int(num) >= 0.5:
    return int(num)+1
  else:
    return int(num)

n = int(sys.stdin.readline().strip())

if n:
  level = []
  for i in range(n):
    level.append(int(sys.stdin.readline().strip()))

  x = solve(n * 0.15)
  level.sort()
  if x > 0:
    print(solve(sum(level[x:-x]) / len(level[x:-x])))
  else:
    print(solve(sum(level) / len(level)))
else:
  print(0)