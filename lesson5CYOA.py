import consoles;
import random;
money = 0
checkOutPrice = 0
print(consoles.ps5items.returns(each[0]))
def startGame(text):
    print(f"Hi, {hello}, welcome to GameStop.\nWe have a PS4, PS5, Xbox One X and Xbox One section.")
    money()

def money():
    print("Your game experience will vary based on the amount of money you recieve. Make your next moves wisely.")
    print("You will recieve 2 different random balances that will contribute to your outcome in this game.\nEven if your credit card amount and cash amount are high, that still won't mean you'll win.")
    cardAmt = random.randint(0, 36)
    cashAmt = random.randint(0, 140)
    totalAmt = cardAmt+cashAmt
    money = totalAmt
    print(f"The amount of money on your card is {cardAmt} and your cash amount is {cashAmt}.\n Your total funds are {totalAmt}")
    print("You win the game by getting home from GameStop with the games in your hand, good luck")

def navigation():
    print("Which aisle would you like to visit first?\nOptions: ps4, ps5, xb1, xb1x")
    print("Your PS5 video game options are Resident Evil: Village - $70 and Batman Arkham Collection - $70\nYour PS4 video game options are Street Fighter 5 - $40 and Call of Duty Black Ops 3 - $25\nYour Xbox One options are Call of Duty Infinite Warfare - $15 and NBA 2K21 - $20\n And lastly Xbox One X which has Gotham Knights - $70 and Mortal Kombat 11 - $36")
    choice = str(input("What is your choice?")).lower()
    while True:
        if choice == "ps5":
            consoles.ps5items.printOptions()
            newChoice = input("Enter (y or n)").lower()
            if newChoice == "y":
                print("Great, these items are added to your cart.")
                checkOutPrice = checkOutPrice+140
                checkout(checkOutPrice)
                break
            else:
                print("Ok, choose the aisle again.")
        elif choice == "ps4":
            consoles.ps4items.printOptions()
            newChoice = input("Enter (y or n)").lower()
            if newChoice == "y":
                print("Great, these items are added to your cart.")
                checkOutPrice = checkOutPrice+140
                checkout(checkOutPrice)
                break
            else:
                print("Ok, choose the aisle again.")
        elif choice == "xb1":
            consoles.xb1items.printOptions()
            newChoice = input("Enter (y or n)").lower()
            if newChoice == "y":
                print("Great, these items are added to your cart.")
                checkOutPrice = checkOutPrice+140
                checkout(checkOutPrice)
                break
            else:
                print("Ok, choose the aisle again.")
        elif choice == "xb1x":
            consoles.xb1xitems.printOptions()
            newChoice = input("Enter (y or n)").lower()
            if newChoice == "y":
                print("Great, these items are added to your cart.")
                checkOutPrice = checkOutPrice+140
                checkout(checkOutPrice)
                break
            else:
                print("Ok, choose the aisle again.")
        else:
            print("Enter a valid option")

def checkout(a):
    if checkOutPrice>money:
        foundOrNot = random.randint(0,2)
        print("You don't have enough, now you'll go outside and look for money\nYou have coinflipped, if it lands on 1, you will find the money, else, you will find another way to get them..")
        print(f"You have rolled a {foundOrNot}")
        if foundOrNot == 0:
            print("Good, you found enough money outside, so you pay and exit.")
            exit()
        else:
            print("You go back to the aisle, get caught and get thrown out. The clerk calls the police on you and you get taken into custody, game over.")
def exit():
    leftRight = input("Do you walk to the left or right side of the street?\tType r for right and l for left")
    while True:
        if leftRight == "r" :
            print("Your games fall into the sewer, oops, game over")
        elif leftRight == "l":
            print("You make it home safe, you win, good job")
hello = input("Welcome, what is your name?")
startGame(hello)
