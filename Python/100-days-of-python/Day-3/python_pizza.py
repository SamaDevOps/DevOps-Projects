print("Welcome to Python Pizza")

pizza_size = input("What size pizza you want? enter S, M or L : ")
pepperroni_topping = input("Do you want pepperoni? enter Y or N : ")
cheese_topping = input("Do you want extra cheese? enter Y or N : ")
bill = 0

if pizza_size == "S":
    bill = 15
    if pepperroni_topping == "Y":
        bill += 2
    if cheese_topping == "Y":
        bill += 1
    print(f"Your final bill is {bill}")
    
elif pizza_size == "M":
    bill = 20
    if pepperroni_topping == "Y":
        bill += 3
    if cheese_topping == "Y":
        bill += 1
    print(f"Your final bill is {bill}")
    
elif pizza_size == "L":
    bill = 25
    if pepperroni_topping == "Y":
        bill += 3
    if cheese_topping == "Y":
        bill += 1
    print(f"Your final bill is {bill}")
