word = input().upper()
set_word = list(set(word))
count_lst = []

for i in set_word:
    count_lst.append(word.count(i))

if 1 < count_lst.count(max(count_lst)):
    print("?")
else:
    print(set_word[count_lst.index(max(count_lst))])