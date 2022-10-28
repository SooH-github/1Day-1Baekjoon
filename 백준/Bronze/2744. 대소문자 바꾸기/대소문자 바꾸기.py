print_word = ""
for i in input():
    if i in "abcdefghijklmnopqrstuvwxyz":
        print_word += i.upper()
    elif i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print_word += i.lower()
print(print_word)