from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turn_on = True

Menu = Menu()
CoffeeMaker = CoffeeMaker()
MoneyMachine = MoneyMachine()

while turn_on:
    order = input(f"What would you like? ({Menu.get_items()}):")
    if order == "off":
        turn_on = False
    elif order == "report":
        CoffeeMaker.report()
        MoneyMachine.report()
    else:
        drink = Menu.find_drink(order)
        if drink:
            if CoffeeMaker.is_resource_sufficient(drink) and MoneyMachine.make_payment(drink.cost):
                CoffeeMaker.make_coffee(drink)

