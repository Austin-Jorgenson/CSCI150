"""This is a module that has 4 functions for games.

There is a function for purchasing items, a shop menu, calling a random monster,
as well as a welcome function. purchase_item is used to define price of item, starting money
and amount you wish to purchase. new_random_monster is used to give a new monster with defined key
values - name, description, health, power, money - print_welcome is passed a str and int and
will give a welcome message for the str centered by the int given. print_shop_menu prints a sign
with two given arguments and prices formatted in a nice sign.

Typical usage examples:
    purchase_item(itemPrice, startingMoney, quantity to purchase)
    monster = new_random_monster()
    print_welcome(name, width)
    print_shop_menu(item1Name, item1Price, item2Name, item2Price)"""

import random

def purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
    """
    Purchases an item from a shop given parameters are met.

    Parameters:
        itemPrice (int): The price of the item wished to purchase.
        startingMoney (int): Amount of money the player has before purchasing.
        quantityToPurchase (int): Amount of item player wants to purchase.
    
    Returns:
        quantityToPurchase
        money_left
    
    Example:
        >>>numPurchased, leftoverMoney = purchase_item(100, 1000, 3)
        >>>print(numPurchased)
        >>>3
    """

    
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
    """Spawns a random monster.

    Parameters:
        none
    
    Returns:
        wild_encounter

    Example:
        >>>encounter = new_random_monster()
        >>>print(encounter['name'])
        >>>print(encounter['description'])
        >>>print(encounter['health'])
        >>>print(encounter['power'])
        >>>print(encounter['money'])
    """

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
    """
    Prints a simple welcome formatted to the center

    Parameters:
        name (str): Enter a name
        width (int): A number of spacing to center the name between
    
    Returns:
        None

    Example:
        >>>print_welcome("Austin", 15)
        >>>   Hello, Austin!  
    """ 

    #adding 'Hello,' and '!' to the name
    greeting = f"Hello, {name}!"

    #printing the greeting with proper format
    print(f"{greeting:^{width}}")



def print_shop_menu(item1name, item1price, item2name, item2price):
    """
    Prints a formatted shop sign

    Parameters:
        item1name (str): Name of first item on sign
        item1price (int): Price of first item on sign
        item2name (str): Name of second item on sign
        item2price (int): Price of second item on sign
    
    Returns:
        None
    
    Example:
        >>>print_shop_menu("Apple", 31, "Pear", 1.234)
        >>>/----------------------\
           | Apple         $31.00 |
           | Pear           $1.23 |
           \----------------------/
    """

    #adding a '$' in front of the price
    price1 = f"${item1price:.2f}"
    price2 = f"${item2price:.2f}"

    #formatting and printing
    print("/", ("-" * 22), "\\", sep="")
    print(f"| {item1name:<12}{price1:>8} |")
    print(f"| {item2name:<12}{price2:>8} |")
    print("\\", ("-" * 22), "/", sep="")



if __name__ == "__main__":
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
