import random

def purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
    """Function takes 3 arguments
(price of item, starting money, and amount you wish to purchase)
and allows you to purchase items
returns number purchased and any leftover money amount"""
    
    numOfItemsPurchaseable = startingMoney // itemPrice
    if 0 < quantityToPurchase < numOfItemsPurchaseable:
        theCost = quantityToPurchase * itemPrice
    elif 0 < numOfItemsPurchaseable < quantityToPurchase:
        theCost = numOfItemsPurchaseable * itemPrice
        quantityToPurchase = numOfItemsPurchaseable
    else:
        theCost = 0
        quantityToPurchase = 0
    money_left = startingMoney - theCost

    return quantityToPurchase, money_left



def new_random_monster():
    """Returns a random monster from a predetermined list
    when assigned to a variable can use options like
    "name" "description" "health" "power" and "money"
    to see various options"""

    #creating list of dictionaries of monsters
    monster_list = [
        {"name": "A cyndaquil", "description": "A small fire mouse",
                      "health": 39, "power": 52, "money": 44},
        {"name": "A totodile", "description": "A big jaw monster",
                       "health": 50, "power": 65, "money": 47},
        {"name": "A chikorita", "description": "A leaf monster",
                      "health": 45, "power": 49, "money": 45}
    ]
    wild_encounter = random.choice(monster_list)

    return wild_encounter



def print_welcome(name, width):
    """Prints a welcome based on two parameters
    (string "name") and (integer "width") and returns
    a centered greeting based on the width chosen
    returns none"""

    #adding 'Hello,' and '!' to the name
    greeting = f"Hello, {name}!"

    #printing the greeting with proper format
    print(f"{greeting:^{width}}")



def print_shop_menu(item1name, item1price, item2name, item2price):
    """Takes four arguments
    item1name(string) item1price(float)
    item2name(string) item2price(float)
    Prints a formatted sign that
    contains both these items and prices
    returns none"""

    #adding a '$' in front of the price
    price1 = f"${item1price:.2f}"
    price2 = f"${item2price:.2f}"

    #formatting and printing
    print("/", ("-" * 22), "\\", sep="")
    print(f"| {item1name:<12}{price1:>8} |")
    print(f"| {item2name:<12}{price2:>8} |")
    print("\\", ("-" * 22), "/", sep="")



#calling function "purchase_item" 3 times
num_purchased, leftover_money = purchase_item(123, 1000, 3)
num_purchased1, leftover_money1 = purchase_item(123, 201, 3)
num_purchased2, leftover_money2 = purchase_item(341, 2112)

#printing the functions
#correct number of items and correct change
print(num_purchased)
print(leftover_money)
print()

#attempting to purchase more items is properly limited
print(num_purchased1)
print(leftover_money1)
print()

#The default value of quantityToPurchase works
print(num_purchased2)
print(leftover_money2)
print()


#calling function "new_random_monster" 3 times
my_monster1 = new_random_monster()
my_monster2 = new_random_monster()
my_monster3 = new_random_monster()

#printing the functions
print(my_monster1['name'])
print(my_monster1['description'])
print()


print(my_monster2['name'])
print(my_monster2['description'])
print(my_monster2['power'])
print()


print(my_monster3['name'])
print(my_monster3['health'])
print(my_monster3['money'])


#calling my function "print_welcome"
print_welcome("Austin", 20)
print_welcome("Jeff", 20)
print_welcome("Kimberly", 20)



#calling my function "print_shop_menu"
print_shop_menu("Apple", 31, "Pear", 1.234)
print_shop_menu("Trash Bags", 73, "Controller", 157.809)
print_shop_menu("Addy Scim", 1561, "Lobbies", 99)
