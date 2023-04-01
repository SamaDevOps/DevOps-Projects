from coffeetypes import MENU

stored_water = {"value" : 300, "unit" : "ml"}
stored_milk = {"value" : 200, "unit" : "ml"}
stored_coffee = {"value" : 100, "unit" : "g"}
stored_money = {"value" : 0, "unit" : "$"}
machine_power = False


def machine_store_stat():
    return (f"Water {stored_water['value']}{stored_water['unit']}\n"
            f"Milk {stored_milk['value']}{stored_milk['unit']}\n"
            f"Coffee {stored_coffee['value']}{stored_coffee['unit']}\n"
            f"Money {stored_money['value']}{stored_money['unit']}\n")
    

def money_stuff(q, d, n, p, drink):
    total = (q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01)
    if total >= MENU[drink]["cost"]:
        print("You have enough money")
        change_money = round((total - MENU[drink]["cost"]), 2)
        stored_money["value"] += MENU[drink]["cost"]
        return f"Here is ${change_money} in change."
    else:
        print("You don't have enough money, Sorry")
    

def brew_coffee(type):
    print(f"You want an {type}")
    if stored_water["value"] > MENU[type]["ingredients"]["water"] and stored_coffee["value"] > MENU[type]["ingredients"]["coffee"]:
        print("good to go")
        print("Please incert coins")
        q = int(input("How many quaters? : "))
        d = int(input("How many dimes? : "))
        n = int(input("How many nickles? : "))
        p = int(input("How many pennies? : "))
        money_check = money_stuff(q, d, n, p, type)
        if money_check:
            print(money_check)
            print(f"Here is your {type}, Enjoy!!!")
            stored_water["value"] -= MENU[type]["ingredients"]["water"]
            stored_coffee["value"] -= MENU[type]["ingredients"]["coffee"]
            


if machine_power:
    user_request = input("What would you like (espresso/latte/cappuccino): ")
else:
    ask_to_start = input("Coffee machine is turned off, Please start first Yes/No :")
    if ask_to_start == "Yes":
        machine_power = True
        user_request = input("What would you like (espresso/latte/cappuccino): ")
        if user_request == "report":
            stat = machine_store_stat()
            print(stat)
        elif user_request == "espresso":
            brew_coffee("espresso")
        elif user_request == "latte":
            brew_coffee("latte")
        elif user_request == "cappuccino":
            brew_coffee("cappuccino")
    else:
        machine_power = False
        



stat = machine_store_stat()
print(stat)