class consoleClass:
    def __init__(self,gameOne,priceOne,gameTwo,priceTwo,gameThree,priceThree,gameFour,priceFour,gameFive,priceFive,gameSix,priceSix,gameSeven,priceSeven,gameEight,priceEight):
        self.gameOne = gameOne
        self.priceOne = priceOne
        self.gameTwo = gameTwo
        self.priceTwo = priceTwo
        self.gameThree = gameThree
        self.priceThree = priceThree
        self.gameFour = gameFour
        self.priceFour = priceFour
        self.gameFive = gameFive
        self.priceFive = priceFive
        self.gameSix = gameSix
        self.priceSix = priceSix
        self.gameSeven = gameSeven
        self.priceSeven = priceSeven
        self.gameEight = gameEight
        self.priceEight = priceEight
    def returns(self):
        each = [self.priceOne,self.priceTwo,self.gameTwo,self.priceTwo,self.gameThree,self.priceThree,self.gameFour,self.priceFour,self.gameFive,self.priceFive,self.gameSix,self.priceSix,self.gameSeven,self.priceSeven,self.gameEight,self.priceEight]
        return each
    def printOptionsPS5(self):
        print(f"Would you like to purchase {self.gameOne} - ${self.priceOne} and {self.gameTwo} ${self.priceTwo}?")
    def printOptionsPS4(self):
        print(f"Would you like to purchase {self.gameThree} - ${self.priceThree} and {self.gameFour} ${self.priceFour}?")
    def printOptionsXB1(self):
        print(f"Would you like to purchase {self.gameFive} - ${self.priceFive} and {self.gameSix} ${self.priceSix}?")
    def printOptionsXB1X(self):
        print(f"Would you like to purchase {self.gameSeven} - ${self.priceSeven} and {self.gameEight} ${self.priceEight}?")
# class ps4game:
#     def __init__(self,gameOne,priceOne,gameTwo,priceTwo):
#         self.gameOne = gameOne
#         self.gameTwo = gameTwo
#         self.priceOne = priceOne
#         self.priceTwo = priceTwo
#     def returns(self):
#         each = [self.priceOne,self.priceTwo]
#         return each
#     def printOptions(self):
#         print(f"Would you like to purchase {self.gameOne} - ${self.priceOne} and {self.gameTwo} ${self.priceTwo}?")
# class xb1game:
#     def __init__(self,gameOne,priceOne,gameTwo,priceTwo):
#         self.gameOne = gameOne
#         self.gameTwo = gameTwo
#         self.priceOne = priceOne
#         self.priceTwo = priceTwo
#     def returns(self):
#         each = [self.priceOne,self.priceTwo]
#         return each
#     def printOptions(self):
#         print(f"Would you like to purchase {self.gameOne} - ${self.priceOne} and {self.gameTwo} ${self.priceTwo}?")
# class xb1xgame:
#     def __init__(self,gameOne,priceOne,gameTwo,priceTwo):
#         self.gameOne = gameOne
#         self.gameTwo = gameTwo
#         self.priceOne = priceOne
#         self.priceTwo = priceTwo
#     def returns(self):
#         each = [self.priceOne,self.priceTwo]
#         return each
#     def printOptions(self):
#         print(f"Would you like to purchase {self.gameOne} - ${self.priceOne} and {self.gameTwo} ${self.priceTwo}?")

# consoleItems = consoleClass("Resident Evil: Village", 70, "Batman Arkham Collection", 71,"Street Fighter 5", 40, "Black Ops 3", 25,"Infinite Warfare", 15, "2K21", 20,"Gotham Knights", 70, "MK11", 36)