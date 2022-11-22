def Rev(x):
    x = str(x)[::-1]
    return int(x)

if __name__ == "__main__":
    x, y = input().split()
    print(Rev(Rev(x) + Rev(y)))