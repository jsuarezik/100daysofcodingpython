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
}

total = 0.00

coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickle": 0.05,
    "penny": 0.01
}


# TODO Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# TODO Turn off the Coffee Machine by entering “off” to the prompt.
# TODO Print report
# TODO Check resources sufficient?
# TODO Process coins.
# TODO Check transaction successful?
# TODO Make Coffee

def print_report():
    """Print a report of the items left on the machine"""
    print("Resources left:")
    for resource in resources:
        print(f"{resource}: {resources[resource]}")
    print(f"Money : ${total}")


def can_make(item):
    """Check if you have enough resources to make item"""
    ingredients = MENU[item]['ingredients']
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, not enough {ingredient}!")
            return False
    return True


def insert_coins():
    """Handle the insertion of coins into the machine"""
    coins_inserted = {}
    print("Please insert coins.")
    for coin in coins:
        amount = int(input(f"How many {coin}s? "))
        coins_inserted[coin] = amount
    return coins_inserted


def get_value_of_coins(coins_inserted):
    """Get the value of the coins inserted"""
    value = 0.00
    for coin in coins:
        value += coins[coin] * coins_inserted[coin]
    return value


def transaction_is_successful(item, value):
    """Check if the transaction is successful"""
    return value >= MENU[item]['cost']


def get_change(item, value):
    """Get change of the price"""
    return round(value - MENU[item]['cost'], 2)


def make_coffee(item):
    """Deducts the ingredients"""
    drink = MENU[item]
    ingredients = drink['ingredients']
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print(f"Here's your {item}, enjoy!")

should_turn_off = False
while not should_turn_off:
    command = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if command == "off":
        should_turn_off = True
    elif command == "report":
        print_report()
    elif command in MENU:
        if can_make(command):
            total_value = get_value_of_coins(insert_coins())
            is_successful = transaction_is_successful(command, total_value)
            if is_successful:
                change = get_change(command, total_value)
                if change > 0.00:
                    print("Here is ${:.2f} in change".format(change))
                total += MENU[command]['cost']
                make_coffee(command)
            else:
                print("Sorry that's not enough money")

    else:
        print("Invalid command")
