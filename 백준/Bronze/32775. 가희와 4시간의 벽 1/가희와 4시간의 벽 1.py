def fourwall(sab, fab):
    return "flight" if sab > fab else "high speed rail"

if __name__ == "__main__":
    sab = int(input())
    fab = int(input())
    
    print(fourwall(sab, fab))