year = int(input("Enter the year you want check : "))

leap = False

if year % 4 == 0:
    leap = True
    if year % 100 != 0:
        leap = True      
        print(f"{year} is a leap year") 
    else:
        leap = False
        if year % 400 == 0:
            leap = True
            print(f"{year} is a leap year")
        else:
            leap = False
            print(f"{year} is not a leap year")
else:
    leap = False
    print(f"{year} is not a leap year")