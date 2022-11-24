def stars(n):
    if n == 1:
        return ["*"]
    
    star = stars(n // 3)
    star_lst = []
    for i in star:
        star_lst.append(i * 3)
    for i in star:
        star_lst.append(i + " " * (n // 3) + i)
    for i in star:
        star_lst.append(i * 3)
    return star_lst
    
if __name__ == "__main__":
    n = int(input())
    print("\n".join(stars(n)))