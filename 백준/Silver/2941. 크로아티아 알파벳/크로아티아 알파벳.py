a_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()

for i in a_list:
    if i in word:
        word = word.replace(i, "1")

print(len(list(word)))