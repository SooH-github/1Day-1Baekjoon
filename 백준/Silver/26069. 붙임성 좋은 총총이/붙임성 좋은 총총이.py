import sys

dance = {"ChongChong"}
for i in range(1, int(sys.stdin.readline()) + 1):
    a, b = sys.stdin.readline().rstrip().split()

    if a in dance:
        dance.add(b)
    if b in dance:
        dance.add(a)

print(len(dance))