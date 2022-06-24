import random
from Player import Player

class AiPlayer(Player):
    def __init__(self, number) -> None:
        super().__init__()
        self.nameHimself(number)
    
    def nameHimself(self, number):
        self.name = "Ai player " + str(number)

    def decideWhetherToExchangeHands(self):
        seed = random.randint(1, 100)
        if seed>70:
            return True
        return False
        

    def show(self):
        card = random.choice(self.hand)
        self.hand.remove(card)
        return card

    def selectAPlayer(self, players):
        return random.choice(players)