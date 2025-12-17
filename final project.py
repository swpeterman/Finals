import random

def final():
    print("Welcome to the adventure game\n")
    print("You are a weary traveler from Goddard, Kansas exploring the lands of Agartha.\n")
    name()
    classes()
    places()


def name():
    try:
        open_file = open("names.txt", "a")
        player_name = input("What is your name traveler? ")
        open_file.write(player_name)
        print("Welcome to your journey through Agartha,", player_name)
        open_file.close()
    except Exception:
        print("Error saving name.")


def classes():
    print("\nPick from the following classes:")
    print("archer\nmage\nknight")
    c = input("What class would you like to be: ")

    if c == "archer" or c == "Archer":
        print("You are granted a bow")
    elif c == "mage" or c == "Mage":
        print("You are granted a staff")
    elif c == "knight" or c == "Knight":
        print("You are granted a sword")
    else:
        print("That choice does not work you are now equipped with a stick.")


def places():
    print("\nYou are presented with 3 different roads.")
    print("1. Monster road")
    print("2. Blue eyed valley")
    print("3. Blonde haired river")

    road = input("Where would you like to take your journey (1, 2, or 3): ")

    if road == "1":
        m_r()
    elif road == "2":
        b_e_y()
    elif road == "3":
        b_h_r()
    else:
        print("Choose a valid place to go")


def m_r():
    print("\nYou decide to travel down the monster road.")
    print("You have encountered a monster!")

    monster_health = random.randint(1, 3)
    print("The monster has", monster_health, "health")

    while monster_health > 0:
        choice = input("Would you like to attack the monster (y/n)? ")

        if choice == "n":
            print("The monster shoots laser beams out of its eyes.")
            print("You have died.")
            return
        elif choice == "y":
            print("You strike the monster!")
            monster_health -= 1
            print("Monster health is now", monster_health)
        else:
            print("Invalid choice.")

    print("You defeated the monster!")
    print("You win!")
    
    choice = input('Would you like to play again: ')
    
    if choice == 'y' or choice == 'Y':
        final()
    else:
        print('Your journey is over. ')

def b_e_y():
    print("\nYou walk into the Blue Eyed Valley.")
    print("The valley is peaceful.")
    print("You rest and recover.")
    print("You win by surviving the journey!")
    
    choice = input('Would you like to play again: ')
    
    if choice == 'y' or choice == 'Y':
        final()
    else:
        print('Your journey is over. ')


def b_h_r():
    print("\nYou arrive at the Blonde Haired River.")
    print("The river is too strong.")
    print("You are swept away by the current.")
    print("Game over.")
    
    choice = input('Would you like to play again: ')
    
    if choice == 'y' or choice == 'Y':
        final()
    else:
        print('Your journey is over. ')


# Start the game
final()
