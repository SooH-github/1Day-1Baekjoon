s = input()
s_set = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        word = s[i:j + 1]
        s_set.add(word)
        
print(len(s_set))