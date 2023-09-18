from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

turn_off = False

while not turn_off:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        turn_off = True
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee_type = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(coffee_type) and money_machine.make_payment(coffee_type.cost):
            coffee_maker.make_coffee(coffee_type)