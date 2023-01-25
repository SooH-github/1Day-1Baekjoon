s = input()

word = []
for i in range(len(s)) :
    word.append(s[i:])

for i in sorted(word):
    print(i)