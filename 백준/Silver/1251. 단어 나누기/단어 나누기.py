word = list(input())
x_word = []
print_word = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        a = word[:i]
        b = word[i:j]
        c = word[j:]
        x_word.append(a[::-1] + b[::-1] + c[::-1])

for i in x_word:
    print_word.append("".join(i))

print(sorted(print_word)[0])