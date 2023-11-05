
print("Welcome to Treasure island.")
print("Your mission is to find the treasure.")
choise1 = input(f"You are at a cross road. Where do you want to go? Type 'left' or 'right'.").lower()

if  choise1 == "left":

choise2 = input("You've come to a lake. There is an island in the middle of the lake."
                " Type 'wait' to wait for a boat. Type 'swim' to swim across.").lower()

if choise2 == "wait":


choise3 = input("You arrive at the island unharmed. "
                "There is a house with 3 doors. One red, one yellow anr one blue. "
                "Wich colour do you choose?").lower()
if  choise3 == "red":

    print("It's a room full of fire. Game Over.")
elif choise3 == "yellow":
    print("You found the treasure! You Win!")

elif choise3 == "blue":
    print("You enter a room of beasts. Game Over.")

    else:
        print("You chose a door that doesn't exist. Game Over.")

    else:
        print("You got attacked by an angry trout. Game Over.")

    else:
        print("You fell into a hole. Game Over")

    else:
        print("You felt into the hole. Game Over.")





