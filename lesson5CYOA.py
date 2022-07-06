import consoles;
import random;
cardAmt = int(random.randint(0, 36))
cashAmt = int(random.randint(0, 145))
balance = cardAmt+cashAmt

def startGame():
    hello = input("Welcome, what is your name? ")
    print(f"Hi, {hello}, welcome to GameStop.\nWe have a PS4, PS5, Xbox One X and Xbox One section.")
    money()

def money():
    print("Your game experience will vary based on the amount of money you recieve. Make your next moves wisely.")
    print("You will recieve 2 different random balances that will contribute to your outcome in this game.\nEven if your credit card amount and cash amount are high, that still won't mean you'll win.")
    print(f"The amount of money on your card is {cardAmt} and your cash amount is {cashAmt}.\n Your total funds are {money}")
    print("You win the game by getting home from GameStop with the games in your hand, good luck")
    navigation()

def navigation():
    print("Which aisle would you like to visit first?\nOptions: ps4, ps5, xb1, xb1x")
    print("Your PS5 video game options are Resident Evil: Village - $70 and Batman Arkham Collection - $70\nYour PS4 video game options are Street Fighter 5 - $40 and Call of Duty Black Ops 3 - $25\nYour Xbox One options are Call of Duty Infinite Warfare - $15 and NBA 2K21 - $20\n And lastly Xbox One X which has Gotham Knights - $70 and Mortal Kombat 11 - $36")
    choice = str(input("What is your choice?")).lower()
    while True:
        if choice == "ps5":
            consoles.consoleItems.printOptionsPS5()
            newChoice = input("Enter (y or n)").lower()
            if newChoice == "y":
                newPrice = 140
                #checkout(newPrice)
                # break
                print("Great, these items are added to your cart.")
                if balance>=newPrice:
                    print("Alright, your bags are bagged and your payment was successful, you may now exit the building")
                    exit()
                else:
                    foundOrNot = int(random.randint(0,2))
                    print("You don't have enough, now you'll go outside and look for money\nYou have coinflipped, if it lands on 1, you will find the money, else, you will find another way to get them..")
                    print(f"You have rolled a {foundOrNot}")
                    if foundOrNot == 0:
                        print("Good, you found enough money outside, so you pay and exit.")
                        exit()
                    else:
                        print("You go back to the aisle, get caught and get thrown out. The clerk calls the police on you and you get taken into custody, game over.")
            else:
                print("Ok, choose the aisle again.")
            break

        elif choice == "ps4":
            consoles.consoleItems.printOptionsPS4()
            newChoice = input("Enter (y or n) ").lower()
            if newChoice == "y":
                print("Great, these items are added to your cart.")
                newPrice = 37
                if balance>=newPrice:
                    print("Alright, your bags are bagged and your payment was successful, you may now exit the building")
                    exit()
                else:
                    foundOrNot = int(random.randint(0,2))
                    print("You don't have enough, now you'll go outside and look for money\nYou have coinflipped, if it lands on 1, you will find the money, else, you will find another way to get them..")
                    print(f"You have rolled a {foundOrNot}")
                    if foundOrNot == 0:
                        print("Good, you found enough money outside, so you pay and exit.")
                        exit()
                    else:
                        print("You go back to the aisle, get caught and get thrown out. The clerk calls the police on you and you get taken into custody, game over.")
            else:
                print("Ok, choose the aisle again.")
            break

        elif choice == "xb1":
            consoles.consoleItems.printOptionsXB1()
            newChoice = input("Enter (y or n)").lower()
            if newChoice == "y":
                print("Great, these items are added to your cart.")
                newPrice = 46
                if balance>=newPrice:
                    print("Alright, your bags are bagged and your payment was successful, you may now exit the building")
                    exit()
                else:
                    foundOrNot = int(random.randint(0,2))
                    print("You don't have enough, now you'll go outside and look for money\nYou have coinflipped, if it lands on 1, you will find the money, else, you will find another way to get them..")
                    print(f"You have rolled a {foundOrNot}")
                    if foundOrNot == 0:
                        print("Good, you found enough money outside, so you pay and exit.")
                        exit()
                    else:
                        print("You go back to the aisle, get caught and get thrown out. The clerk calls the police on you and you get taken into custody, game over.")
            else:
                print("Ok, choose the aisle again.")
            break

        elif choice == "xb1x":
            consoles.consoleItems.printOptionsXB1X()
            newChoice = input("Enter (y or n)").lower()
            if newChoice == "y":
                print("Great, these items are added to your cart.")
                newPrice = 151
                if balance>=newPrice:
                    print("Alright, your bags are bagged and your payment was successful, you may now exit the building")
                    exit()
                else:
                    foundOrNot = int(random.randint(0,2))
                    print("You don't have enough, now you'll go outside and look for money\nYou have coinflipped, if it lands on 1, you will find the money, else, you will find another way to get them..")
                    print(f"You have rolled a {foundOrNot}")
                    if foundOrNot == 0:
                        print("Good, you found enough money outside, so you pay and exit.")
                        exit()
                    else:
                        print("You go back to the aisle, get caught and get thrown out. The clerk calls the police on you and you get taken into custody, game over.")
            else:
                print("Ok, choose the aisle again.")

        else:
            print("Enter a valid option")
        break

# def checkout(a):
#     if balance>=newPrice:
#         print("Alright, your bags are bagged and your payment was successful, you may now exit the building")
#         exit()
#     else:
#         foundOrNot = int(random.randint(0,2))
#         print("You don't have enough, now you'll go outside and look for money\nYou have coinflipped, if it lands on 1, you will find the money, else, you will find another way to get them..")
#         print(f"You have rolled a {foundOrNot}")
#         if foundOrNot == 0:
#             print("Good, you found enough money outside, so you pay and exit.")
#             exit()
#         else:
#             print("You go back to the aisle, get caught and get thrown out. The clerk calls the police on you and you get taken into custody, game over.")

def exit():
    leftRight = input("Do you walk to the left or right side of the street?\tType r for right and l for left")
    if leftRight == "r" :
        print("Your games fall into the sewer, oops, game over")
    elif leftRight == "l":
        print("You make it home safe, you win, good job")

startGame()