n = int(input())

count = 1
honey_num = 1
while honey_num < n:
    honey_num += count * 6
    count += 1

print(count)