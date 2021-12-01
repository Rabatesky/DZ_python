year = int(input())
if year < 0:
    print("")
else:
    if year % 400 == 0:
        print("год високосный")
    elif year % 100 == 0:
        print("год не високосный")
    elif year % 4 == 0:
        print("Год високосный")
    else:
        print("Год не високосный")