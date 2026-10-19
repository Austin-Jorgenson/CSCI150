import gamefunctions

user = input("Please enter your name: ")
number = int(input("Please enter a number: "))
remainingMoney = 1000

gamefunctions.print_welcome(user, number)

monster = gamefunctions.new_random_monster()
inspect = input(f"{monster['name']} appeared:\nInspect? (y/n)")



if inspect == "y":
    print(f"{monster['description']} health-{monster['health']} power-{monster['power']} money-{monster['money']}")
    pass
else:
    print(f"{monster['name']} fled")
    pass


readsign = input("You walk up to a shop sign\nRead? (y/n)")

if readsign == "y":
    shopsign = gamefunctions.print_shop_menu("Pokeball", 200, "Potion", 300)
    shopPrompt = input("Would you like to purchase an item? (y/n)")
    if shopPrompt == "y":
        print("Starter money $1000")
        itemChoice = input("What would you like to purchase?: ")
        itemAmount = int(input("How many would you like to purchase?: "))
        if itemChoice == "Pokeball":
            numPurchased, remainingMoney = gamefunctions.purchase_item(200, remainingMoney, itemAmount)
            print(f"Purchased: {numPurchased} Money remaining: {remainingMoney}")
        elif itemChoice == "Potion":
            numPurchased, remainingMoney = gamefunctions.purchase_item(300, remainingMoney, itemAmount)
            print(f"Purchased: {numPurchased} Money remaining: {remainingMoney}")
        else:
            print("That is not a valid option")
else:
    print("You walk past the sign and continue on your journey")



