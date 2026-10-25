import gamefunctions
import random

characterDamage = 8
characterHealth = 75
characterGold = 0

def print_menu():
    """
    Prints a menu for options in town to be called

    Parameters - None

    Returns - None
    
    """
    print("""
1. Enter tall grass
2. Sleep (Restore HP for 50 gold)
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
3. Check Status
    """)
    
def enter_battle():
    """
    Enters user into a battle loop with preset damage health and gold
    Gives options for attacking, fleeing, and checking status

    Parameters - None

    Returns - None

    """
    global characterDamage, characterHealth, characterGold
    monster = gamefunctions.new_random_monster()
    monsterHealth = monster['health']
    monsterDamage = monster['power'] // 10
    print(f"{monster['name'].strip()} appears")
    while characterHealth > 0 and monsterHealth > 0:
        print(f"User health - {characterHealth}\n{monster['name']} health - {monsterHealth}")
        battle_menu()
        battleChoice = input("What would you like to do?: ").strip().lower()
        if battleChoice == "1":
            monsterHealth -= characterDamage
            characterHealth -= monsterDamage
        elif battleChoice == "2":
            print("You fled the battle\n")
            break # exits the while loop
        elif battleChoice == "3":
            print("Still great :)")
        else:
            print("Unrecognized command")
    if characterHealth <= 0:
        if characterGold < 35:
            print(f"You whited out...\nDropped {characterGold} gold.\n")
            characterGold = 0
            characterHealth = 75
        elif characterGold >= 35:
            print("You whited out...\nDropped 35 gold.\n")
            characterGold -= 30
            characterHealth = 75
    elif monsterHealth <= 0:
        print(f"You have beaten {monster['name']}")
        characterGold += monster['money']
        print(f"Gained {monster['money']} gold\n")

def rest():
    """
    Allows a user to restore HP if they have 50 gold

    Parameters - None

    Returns - None

    """
    global characterHealth, characterGold
    if characterGold < 50:
        print("You do not have enough gold.\n")
    elif characterGold >= 50:
        characterHealth = 75
        characterGold -= 50
        print("You took a nap. You are no longer tired.\n")
    


    
if __name__ == "__main__":
        while True:
            print(f"You are in New Bark Town.\nCurrent HP: {characterHealth} Current Gold: {characterGold}")
            print_menu()
            menuChoice = input("What is your choice?: ").strip().lower()
            if menuChoice == "1":
                enter_battle()
            elif menuChoice == "2":
                rest()
            elif menuChoice == "q":
                break
            else:
                print("Invalid choice. Try again.")
print("Thanks for playing!")