# Height check
print("Welcome to RollerCoaster ride!")

height = int(input("Please enter your height in cm : "))

if height > 120:
    print("You are good to go")
    age_check = int(input("Please enter your age: "))
    if age_check < 12:
        print("please pay 5 dollers")
    elif 12 <= age_check <= 18:
        print("please pay 10 dollers")
    elif age_check > 18:
        print("please pay 15 dollers")
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
