def star(x):
    if x == 3:
        return ["  *  ", " * * ", "*****"]

    xx = star(x // 2)
    s_lst = []
    for i in xx:
        s_lst.append(" " * (x // 2) + i + " " * (x // 2))

    for i in xx:
        s_lst.append(i + " " + i)

    return s_lst

if __name__ == "__main__":
    print("\n".join(star(int(input()))))