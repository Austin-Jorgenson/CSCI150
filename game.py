import gamefunctions
import random
import copy

characterDamage = 8

state = {
    "characterHealth": 75,
    "characterGold": 500,
    "characterInventory": [
        
    ]
}

def print_menu():
    """
    Prints a menu for options in town to be called

    Parameters - None

    Returns - None
    
    """
    print("""
1. Enter tall grass
2. Sleep (Restore HP for 50 gold)
3. View inventory
4. Shop
q. Quit
    """)

def battle_menu():
    """
    Prints a menu for three options to be called

    Parameters - None

    Returns - None
    
    """
    print("""
1. Attack
2. Flee
3. Use Item
    """)
    
def enter_battle():
    """
    Enters user into a battle loop with preset damage health and gold
    Gives options for attacking, fleeing, and checking status

    Parameters - None

    Returns - None

    """
    monster = gamefunctions.new_random_monster()
    monsterDamage = monster['power'] // 10
    print(f"{monster['name'].strip()} appears")
    while state["characterHealth"] > 0 and monster['health'] > 0:
        print(f"User health - {state['characterHealth']}\n{monster['name']} health - {monster['health']}")
        battle_menu()
        battleChoice = input("What would you like to do?: ").strip().lower()
        if battleChoice == "1":
            currentDamage = characterDamage
            for item in state["characterInventory"]:
                if item.get("name") == "sword" and item.get("equipped") == "yes":
                    currentDamage += 10
                    
                    item["usesLeft"] -= 1   #lowering uses on weapon breaking if needed
                    if item["usesLeft"] <= 0:
                        print("Your sword broke.")
                        state["characterInventory"].remove(item)
                    break #breaks out of item check
            monster['health'] -= currentDamage
            state["characterHealth"] -= monsterDamage
        elif battleChoice == "2":
            print("You fled the battle\n")
            break # exits the while loop
        elif battleChoice == "3":
            consumableItem(state, monster)
            

        else:
            print("Unrecognized command")
    if state["characterHealth"] <= 0:
        if state["characterGold"] < 35:
            print(f"You whited out...\nDropped {characterGold} gold.\n")
            state["characterGold"] = 0
            state["characterHealth"] = 75
        elif state["characterGold"] >= 35:
            print("You whited out...\nDropped 35 gold.\n")
            state["characterGold"] -= 30
            state["characterHealth"] = 75
    elif monster['health'] <= 0:
        print(f"You have beaten {monster['name']}")
        state["characterGold"] += monster['money']
        print(f"Gained {monster['money']} gold\n")

def rest():
    """
    Allows a user to restore HP if they have 50 gold

    Parameters - None

    Returns - None

    """
    if state['characterHealth'] == 75:
        print("You already have full health.\n")
    elif state['characterHealth'] < 75:
        if state["characterGold"] < 50:
            print("You do not have enough gold.\n")
        elif state["characterGold"] >= 50:
            state["characterHealth"] = 75
            state["characterGold"] -= 50
            print("You took a nap. You are no longer tired.\n")

def viewInventory():
    """
    Allows a user to view their inventory

    Parameters - None

    Returns - None

    """
    if not state.get("characterInventory"):
        print("Your inventory is empty\n")
        return

    if state["characterInventory"]:
        for item in state["characterInventory"]:
            print(f"{item}\n")
        userChoice = input("Would you like to equip an item? (Y/N): ").lower()
        if userChoice == "y":
            #check if user has equipable items
            equipableChoices = []
            for item in state["characterInventory"]:
                if item.get("type") == "equipable":
                    equipableChoices.append(item)
            if not equipableChoices:
                print("You do not have any equipable items.\n")
                return
            
            itemNum = 1
            for item in equipableChoices:
                print(f"{itemNum}: {item}")
                itemNum += 1
            print()

            equippedChoice = int(input("Enter the number of the item you wish to equip: "))
            selectedItem = equipableChoices[equippedChoice - 1]

            for item in state["characterInventory"]:
                if item.get("equipped") == "yes":
                    print(f"Unequipped {item['name']}.")
                    item["equipped"] = "no"

            selectedItem["equipped"] = "yes"
            equippedItem = selectedItem["name"]
            print(f"Successfully equipped {equippedItem}.\n")

def shop():
    """
    Has a shop with a two item menu
    player can purchase

    Parameters - None

    Returns - None

    """
    gamefunctions.print_shop_menu("Sword", 350, "OneShot", 450)
    shopInventory = [
        {"name": "sword","usesLeft": 10, "type": "equipable", "equipped": "no", "value": 350},
        {"name": "OneShot", "usesLeft": 1, "type": "consumable", "value": 450}
    ]
    
    while state['characterGold'] > 0:
        print(f"Current Gold: {state['characterGold']}")
        buyChoice = input("Please select a choice:\n1. Sword\n2. OneShot\nq. Exit Shop\n")
        if buyChoice == "q":
            print("Thank you for coming in.")
            break # letting the user quit out
        buyAmount = int(input("How many would you like to purchase?\n"))

        itemChoice = None
        if buyChoice == "1":
            itemChoice = shopInventory[0]
        elif buyChoice == "2":
            itemChoice = shopInventory[1]

        if itemChoice is not None:
            itemName = itemChoice.get("name")
            itemCost = itemChoice.get("value", 10000)

        numPurchased, state['characterGold'] = gamefunctions.purchase_item(itemCost, state['characterGold'], buyAmount)

        if numPurchased > 0:
            for i in range(numPurchased):
                state['characterInventory'].append(copy.deepcopy(itemChoice))
            print(f"Bought {numPurchased} {itemName}")


            


        else:
            print(f"You don't have enough gold to purchase {buyAmount} {itemName}")
        print()

    if state['characterGold'] <= 0:
        print("You have no gold to spend, stop loitering.")

def consumableItem(gameState, monster):
    for i, item in enumerate(state['characterInventory']):
        if(item['type'] == 'consumable'):
            print(i, item)
    user_choice = input("Choose an item\n")
    if i <= len(state['characterInventory']) and state['characterInventory'][i]:
        item = state['characterInventory'][i]
        if(item['name'] == 'OneShot'):
            monster['health'] -= 5000
        state['characterInventory'].pop(i)

    
if __name__ == "__main__":
        while True:
            print(f"You are in New Bark Town.\nCurrent HP: {state['characterHealth']} Current Gold: {state['characterGold']}")
            print_menu()
            menuChoice = input("What is your choice?: ").strip().lower()
            if menuChoice == "1":
                enter_battle()
            elif menuChoice == "2":
                rest()
            elif menuChoice == "3":
                viewInventory()
            elif menuChoice == "4":
                shop()
            elif menuChoice == "5":
                pass
            elif menuChoice == "q":
                break
            else:
                print("Invalid choice. Try again.")
print("Thanks for playing!")