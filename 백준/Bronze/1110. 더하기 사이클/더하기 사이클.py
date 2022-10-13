n = input()
if int(n) < 10:
    n = "0" + n

count = 1
n2_lst = [n[1] + str(int(n[0]) + int(n[1]))[-1]]
while n != n2_lst[-1]:
    n2 = n2_lst[-1]
    n2_lst.append(n2[1] + str(int(n2[0]) + int(n2[1]))[-1])
    count += 1
    
print(count)