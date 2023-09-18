MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

espresso_water = MENU['espresso']['ingredients']['water']
espresso_coffee = MENU['espresso']['ingredients']['coffee']
latte_water = MENU['latte']['ingredients']['water']
latte_milk = MENU['latte']['ingredients']['milk']
latte_coffee = MENU['latte']['ingredients']['coffee']
cappuccino_water = MENU['cappuccino']['ingredients']['water']
cappuccino_milk = MENU['cappuccino']['ingredients']['milk']
cappuccino_coffee = MENU['cappuccino']['ingredients']['coffee']


def check_resources(ingredients):
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}. \n")
            return False
    return True


def process_money():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))*0.25
    dimes = int(input("how many dimes?: "))*0.1
    nickles = int(input("how many nickles?: "))*0.05
    pennies = int(input("how many pennies?: "))*0.01
    total = quarters + dimes + nickles + pennies
    return total


def is_transaction_successful(money_inserted, drink_cost):
    if money_inserted >= drink_cost:
        change = round(money_inserted - drink_cost, 2)
        print(f"Here is ${change} in change.")
        resources["money"] += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_type, order_ingredients):
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here is your {drink_type} ☕️. Enjoy!")


turn_off = False

while not turn_off:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        turn_off = True
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    else:
        coffee_type = MENU[user_choice]
        if check_resources(coffee_type["ingredients"]):
            money_paid = process_money()
            if is_transaction_successful(money_paid, coffee_type["cost"]):
                make_coffee(user_choice, coffee_type["ingredients"])
