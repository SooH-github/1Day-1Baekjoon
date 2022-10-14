num_lst = []
for i in range(10):
    num_lst.append(int(input()) % 42)
    
print(len(set(num_lst)))