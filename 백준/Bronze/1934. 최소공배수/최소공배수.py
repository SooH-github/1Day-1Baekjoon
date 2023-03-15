for i in range(int(input())):
    a, b = map(int, input().split())
    A, B = a, b
    
    while a != 0:
        b = b % a
        a, b = b, a   

    print(A * B //b)