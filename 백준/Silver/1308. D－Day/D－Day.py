def is_day_count(yyyymmdd):
    year = int(yyyymmdd[0])
    ytod = (year - 1) * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
    
    month = int(yyyymmdd[1])
    mtod = 0
    for i in range(1, month):
        if i == 2:
            if year % 400 == 0:
                mtod += 29
            elif year % 100 == 0:
                mtod += 28
            elif year % 4 == 0:
                mtod += 29
            else:
                mtod += 28
        elif i in [4, 6, 9, 11]:
            mtod += 30
        else:
            mtod += 31

    day = int(yyyymmdd[2])

    return ytod + mtod + day

def is_date_sub(first_date, second_date):
    if 1000 < int(second_date[0]) - int(first_date[0]):
        print("gg")
    elif int(second_date[0]) - int(first_date[0]) == 1000 and int(f"{first_date[1]}{first_date[2]}") <= int(f"{second_date[1]}{second_date[2]}"):
        print("gg")
    else:
        print(f"D-{abs(is_day_count(first_date) - is_day_count(second_date))}")

if __name__ == '__main__':
    first_date = list(input().split())
    second_date = list(input().split())
    is_date_sub(first_date, second_date)  