while True:
    name, age, kg = input().split()
    if name == "#" and age == "0" and kg == "0":
        break
    
    if 17 < int(age) or 80 <= int(kg):
        print(f"{name} Senior")
    else:
        print(f"{name} Junior")