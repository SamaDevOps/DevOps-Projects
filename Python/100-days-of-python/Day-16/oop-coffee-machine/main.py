from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
all_items = menu.get_items()
coffee_machine = CoffeeMaker()
money_collector = MoneyMachine()

selected_coffee = input(f"Please select the coffee type you want {all_items} : ")
drink_data = menu.find_drink(selected_coffee)

if coffee_machine.is_resource_sufficient(drink_data):
    print(f"Cost of {selected_coffee} is {drink_data.cost}")
    if money_collector.make_payment(drink_data.cost):
        coffee_machine.make_coffee(drink_data)

print(coffee_machine.report())
