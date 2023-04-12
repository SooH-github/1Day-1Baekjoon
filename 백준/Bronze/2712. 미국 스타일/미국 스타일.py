for i in range(int(input())):
    n, u = input().split()
    if u == "kg":
        print("%.4f lb" % (float(n) * 2.2046))
    elif u == "lb":
        print("%.4f kg" % (float(n) * 0.4536))
    elif u == "l":
        print("%.4f g" % (float(n) * 0.2642))
    elif u == "g":
        print("%.4f l" % (float(n) * 3.7854))