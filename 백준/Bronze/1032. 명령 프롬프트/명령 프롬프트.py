n = int(input())
word = list(input())
             
for i in range(n - 1):
    other = list(input())
    for j in range(len(word)):
        if word[j] != other[j]:
            word[j] = "?"

print("".join(word))