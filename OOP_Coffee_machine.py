from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Creating all objects.
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
continuing = True

while continuing:
    user = input(f'What would you like? {menu.get_items()}): ').lower()

    # Multiple options to do things.
    if user == "report":
        coffee_maker.report()
        money_machine.report()
    elif user == "off":
        continuing = False
    else:
        # this returns the item, and drink holds onto that value
        drink = menu.find_drink(user)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

