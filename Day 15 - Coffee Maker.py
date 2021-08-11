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
    "water": 1500,
    "milk": 300,
    "coffee": 500,
}

QUARTER = 0.25
DIME = 0.1
NICKEL = 0.05
PENNY = 0.01

INGREDIENTS = "ingredients"
COST = "cost"
WATER = "water"
MILK = "milk"
COFFEE = "coffee"
TOTAL_WATER = resources[WATER]
TOTAL_MILK = resources[MILK]
TOTAL_COFFEE = resources[COFFEE]
TOTAL_MONEY = 0

user = "on"


def start():
    print("Type 'off' to turn off,\nor 'report' to see the remaining items and money collected.\n")

    global user
    user = input("What would you like? (espresso/latte/cappuccino): ").lower()

    possible_inputs = ["off", "report", "latte", "cappuccino", "espresso"]
    if user not in possible_inputs:
        print("Invalid Input\n")
        return start()
    if user == "off":
        return

    def report():
        print(f"Water: {TOTAL_WATER}\nMilk: {TOTAL_MILK}\nCoffee: {TOTAL_COFFEE}\nMoney: {TOTAL_MONEY}\n")
    if user == "report":
        report()
        return start()
    item = MENU[user]

    def cost():
        global TOTAL_COFFEE, TOTAL_WATER, TOTAL_MILK, TOTAL_MONEY
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        if (quarters not in range(1000)) or (dimes not in range(1000)) or (nickels not in range(1000)) or (pennies not in range(1000)):
            print("Invalid input\n")
            return start()
        total_paid = (quarters*QUARTER)+(dimes*DIME)+(nickels*NICKEL)+(pennies*PENNY)
        if total_paid < item["cost"]:
            print(f'Sorry the cost is ${item["cost"]}. You only paid ${"{:.2f}".format(total_paid)}, so here is your money back.\n')
            return start()
        elif total_paid >= item['cost']:
            if total_paid > item['cost']:
                print(f"Here is your change ${'{:.2f}'.format(total_paid-item['cost'])}.")
            print(f"Here is your {user}☕, ENJOY!\n")
            TOTAL_COFFEE -= item[INGREDIENTS][COFFEE]
            TOTAL_WATER -= item[INGREDIENTS][WATER]
            if user != "espresso":
                TOTAL_MILK -= item[INGREDIENTS][MILK]
            TOTAL_MONEY += item["cost"]
            return start()

    def coffee():

        global TOTAL_COFFEE, TOTAL_WATER, TOTAL_MILK, TOTAL_MONEY
        remaining_resources = [TOTAL_WATER, TOTAL_MILK, TOTAL_COFFEE]
        i = -1
        for ingredient in item["ingredients"]:
            i += 1
            if item["ingredients"][ingredient] > remaining_resources[i]:
                print(f"Sorry out of {ingredient}.")
                refill = input("Type 'refill' to refill, or 'quit' to quit.\n")
                if refill == "refill":
                    TOTAL_WATER = resources[WATER]
                    TOTAL_MILK = resources[MILK]
                    TOTAL_COFFEE = resources[COFFEE]
                elif refill == "quit":
                    return start()
                else:
                    print("Invalid input.\n")
                    return start()
        cost()

    coffee()


start()
