import consoles;
import random;
money = 0

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
            newChoice = input("Enter (y or n)")
            pass
        elif choice == "ps4":
            consoles.ps4items.printOptions()
            newChoice = ("Enter (y or n)")
            pass
        elif choice == "xb1":
            consoles.xb1items.printOptions()
            newChoice = input("Enter (y or n)")
            pass
        elif choice == "xb1x":
            consoles.xb1xitems.printOptions()
            newChoice = input("Enter (y or n)")
            pass
        else:
            print("Enter a valid option")

hello = input("Welcome, what is your name?")
startGame(hello)
