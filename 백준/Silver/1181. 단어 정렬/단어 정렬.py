word_lst = []
for i in range(int(input())):
    word_lst.append(input())

print_lst = sorted(sorted(set(word_lst)), key = lambda x : len(x))
for i in print_lst:
    print(i)