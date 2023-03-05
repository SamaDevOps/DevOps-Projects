# numbers = input("Please Enter the number : ").split(",")
numbers = range(1,101)

for number in numbers:
    valuvator = int(number)
    if valuvator % 3 == 0 or valuvator % 5 == 0:
        if valuvator % 3 == 0:
            print("Fizz")
        if valuvator % 5 == 0:
            print("Buzz")
    else:
        print(valuvator)
