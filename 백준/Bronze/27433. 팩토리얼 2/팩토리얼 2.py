def fac(num):
    if num == 0:
        return 1
    else:
        f_num = 1
        while num > 0:
            f_num *= num
            num -= 1
        return f_num

if __name__ == "__main__":
    print(fac(int(input())))