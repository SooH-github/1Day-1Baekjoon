word = input()
alpha = "aeiou"
cnt = 0

for i in alpha:
    cnt += word.count(i)
print(cnt)