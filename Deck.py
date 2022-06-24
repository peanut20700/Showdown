
from enum import Enum
from random import shuffle
from Card import Card
from Rank import Rank
from Suit import Suit


class Result(Enum):
    Lose  = -1
    Tie   =  0
    Win   =  1

class Deck:
    def __init__(self, cards) -> None:
        self.cards = None
        self.setCards(cards)

    def shuffle(self):
        shuffle(self.cards)

    def drawCard(self):
        if not self.cards:
            print("Deck is empty !")
            return None
        return self.cards.pop()

    def getCards(self):
        return self.cards

    def setCards(self, cards):
        self.cards = cards
