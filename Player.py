from abc import ABC, abstractclassmethod

from Hand import Hand
from ExangeHands import ExangeHands

class Player(ABC):
    def __init__(self) -> None:
        self.name = None
        self.point = 0
        self.hand = list()
        self.alreadyExchanged = False
        self.exangeHands = None
    
    def getName(self):
        return self.name

    def setHand(self, hand):
        self.hand = hand
    
    def getHand(self):
        return self.hand
    
    def takeTurn(self):
        return self.show()

    def addHand(self, card):
        self.hand.append(card)

    def setAlreadyExchanged(self, alreadyExchanged):
        self.alreadyExchanged = alreadyExchanged
    
    def getAlreadyExchanged(self):
        return self.alreadyExchanged

    def gainPoint(self):
        self.point += 1
    
    def getPoint(self):
        return self.point

    def setExchangeHands(self, exangeHands):
        self.exangeHands = exangeHands

    def getExchangeHands(self):
        return self.exangeHands

    @abstractclassmethod
    def nameHimself(self):
        pass

    @abstractclassmethod
    def decideWhetherToExchangeHands(self):
        pass

    @abstractclassmethod
    def show(self):
        pass

    @abstractclassmethod
    def selectAPlayer(self, players):
        pass

