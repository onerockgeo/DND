import random

# Our main function.
def main():
    menu()


# Roll the dice.
def roll():
    print("\nRolling 4d6 - Dropping Lowest")
    dice = []
    for x in range(0, 4): # 4 Dice rolls per row
        column = []
        for y in range(0, 4): # How many dice rolls per set.
            column.append(random.randint(1,6))
        dice.append(column)
        #print(dice)
    findLowest(dice)


# Calculates the point buy cost.
def calcPointBuy(score):
    if(score < 14):
        return (score - 8)
    elif(score == 14):
        return 7
    elif(score == 15):
        return 9
    else:
        return score - 6


# Find lowest number in each row and ignore it, then total the row.
def findLowest(diceRolls):
    total = 0
    pbt = 0
    for x in range(0,4):
        smallest = diceRolls[x]
        smallest.sort()
        for i in range(1,4): # Skip the first element since it's the smallest after sorting.
            total += smallest[i]
        print(diceRolls[x], "(drop)", *smallest[:1], "Total: ", total, ", point buy cost = ", calcPointBuy(total)) # Print the dice roll
        pbt += calcPointBuy(total) # Add the value of the last set of dice to the point buy total.
        total = 0
    print("Point Buy Total = ", pbt)


# This will be the point buy system.
def pbs():
    print("\n\nPoint buy system...")
    print("To be implemented...")


# Main Menu
def menu():
        ans = True
        print("Welcome to the Taters! D&D 5e Ability Score Roller")
        print("Now written in Python")
        while ans:
            print("""\n1. Roll the dice
2. Use point buy system
3. Exit
            """)
            choice = input("Please select an option: ")
            if choice == '1':
                roll()
            elif choice == '2':
                pbs()
            elif choice == '3':
                exit()
            else:
                print("Unknown option selected!")

main()
