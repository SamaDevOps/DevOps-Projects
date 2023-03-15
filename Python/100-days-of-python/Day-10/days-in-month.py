def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        

year = int(input("Enter a year : "))
month = int(input("Enter a month : "))
month_normal = ["31","28","31","30","31","30","31","31","30","31","30","31"]
month_leap = ["31","29","31","30","31","30","31","31","30","31","30","31"]

def day_cal(year,month):
    check_leap = is_leap(year)
    if check_leap:
        days = month_leap[month - 1]
    else:
        days = month_normal[month-1]
    return days

out = day_cal(year=year,month=month)

print(out)

