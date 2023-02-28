# Height check
print("Welcome to RollerCoaster ride!")

height = int(input("Please enter your height in cm : "))
bill = 0

if height > 120:
    print("You are good to go")
    age_check = int(input("Please enter your age: "))
    if age_check < 12:
        bill = 5
        print("child ticket is 5 dollers")
    elif 12 <= age_check <= 18:
        bill = 10
        print("youth ticket is 10 dollers")
    elif age_check > 18:
        bill = 15
        print("adult ticket is 15 dollers")
    
    want_a_photo = input("Please Enter 'Y' if you want a photo or 'N' to No : ")
    if want_a_photo == "Y":
        bill += 3
    
    print(f"Your total bill is {bill}")
    
else:
    print("Not tall enough")
    
print("\n------------------------\n")

# Odd or even

print("Odd or Even Number Checker")

value_to_test = int(input("Enter a number you want to check : "))

if (value_to_test % 2) == 0:
    print("This is a even number")
else:
    print("This is a odd number")
