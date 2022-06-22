from numpy import number
from Player import Player
from ValidateInputUtils import ValidateInputUtils

class HumanPlayer(Player):
    def __init__(self) -> None:
        super().__init__()
    
    def nameHimself(self):
        username = input("Enter username: ")
        self.name = username

    def decideWhetherToExchangeHands(self) -> bool:
        changeOrNot = input("do you want to change your hand with someone? y/n ")
        while changeOrNot != 'y' and changeOrNot != 'n':
            print("invalid input")
            changeOrNot = input("do you want to change your hand with someone? y/n ")
        if changeOrNot == 'y':
            self.setAlreadyExchanged(True)
            return True
        return False

    def show(self):
        for i in range(len(self.hand)):
            print(str(i+1) + " " + self.hand[i].getSuit().name + " " +  self.hand[i].getRank().name)
        selected = input("show 1 card from your hand : ")
        while not ValidateInputUtils.numberShouldBetween(1, len(self.hand), selected):
            print("input should between 1 ~ " + str(len(self.hand)))
            selected = input("show 1 card from your hand : ")
        card = self.hand.pop(int(selected)-1)
        return card
    
    def selectAPlayer(self, players):
        for i in range(len(players)):
            print(str(i+1) + " "  + players[i].getName())
        selectedPlayer = input("select a player to change hand with him: ")
        while not ValidateInputUtils.numberShouldBetween(1, len(players), selectedPlayer):
            print("input should between 1 ~ " + str(len(players)))
            selected = input("select a player to change hand with him: ")
        return players[int(selectedPlayer)-1]
