n_lst = ["a", "e", "i", "o", "u"]

while True:
    n = input()
    if n == "#":
        break
    n_sum = 0
    for i in n.lower():
        if i in n_lst:
            n_sum += 1
    print(n_sum)