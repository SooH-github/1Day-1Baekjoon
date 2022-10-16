s = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"

print_lst = []
for i in alphabet:
    print_lst.append(str(s.find(i)))

print(' '.join(print_lst))