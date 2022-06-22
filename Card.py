class Card:
    def __init__(self) -> None:
        self.rank = None
        self.suit = None

    def setSuit(self, suit):
        self.suit = suit
    
    def getSuit(self):
        return self.suit
    
    def setRank(self, rank):
        self.rank = rank
    
    def getRank(self):
        return self.rank

    def showdown(self, card) -> bool:
        if self.getRank().value > card.getRank().value:
            return True
        elif self.getRank().value < card.getRank().value:
            return False
        else:
            if self.getSuit().value > card.getSuit().value:
                return True
            elif self.getSuit().value < card.getSuit().value:
                return False
