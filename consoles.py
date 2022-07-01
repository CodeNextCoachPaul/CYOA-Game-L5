class ps5game:
    def __init__(self,gameOne,priceOne,gameTwo,priceTwo):
        self.gameOne = gameOne
        self.priceOne = priceOne
        self.gameTwo = gameTwo
        self.priceTwo = priceTwo
    def printOptions(self):
        print(f"Would you like to purchase {self.gameOne} - $ {self.priceOne} and {self.gameTwo} ${self.priceTwo}?")
class ps4game:
    def __init__(self,gameOne,priceOne,gameTwo,priceTwo):
        self.gameOne = gameOne
        self.gameTwo = gameTwo
        self.priceOne = priceOne
        self.priceTwo = priceTwo
    def printOptions(self):
        print(f"Would you like to purchase {self.gameOne} - ${self.priceOne} and {self.gameTwo} ${self.priceTwo}?")
class xb1game:
    def __init__(self,gameOne,priceOne,gameTwo,priceTwo):
        self.gameOne = gameOne
        self.gameTwo = gameTwo
        self.priceOne = priceOne
        self.priceTwo = priceTwo
    def printOptions(self):
        print(f"Would you like to purchase {self.gameOne} - ${self.priceOne} and {self.gameTwo} ${self.priceTwo}?")
class xb1xgame:
    def __init__(self,gameOne,priceOne,gameTwo,priceTwo):
        self.gameOne = gameOne
        self.gameTwo = gameTwo
        self.priceOne = priceOne
        self.priceTwo = priceTwo
    def printOptions(self):
        print(f"Would you like to purchase {self.gameOne} - ${self.priceOne} and {self.gameTwo} ${self.priceTwo}?")

ps5items = ps5game("Resident Evil: Village", 70, "Batman Arkham Collection", 70)
ps4items = ps4game("Street Fighter 5", 40, "Black Ops 3", 25)
xb1items = xb1game("Infinite Warfare", 15, "2K21", 20)
xb1xitems = xb1xgame("Gotham Knights", 70, "MK11", 36)