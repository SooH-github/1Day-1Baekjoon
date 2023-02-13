cute = []
for i in range(int(input())):
    cute.append(int(input()))

if cute.count(0) < cute.count(1):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")