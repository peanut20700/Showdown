
from cgi import test
from random import shuffle
from HumanPlayer import HumanPlayer
from AiPlayer import AiPlayer
from Deck import Deck
from ExangeHands import ExangeHands

class Showdown:
    def __init__(self, players, deck) -> None:
        self.round = 1
        self.maxRound = 13
        self.players = list()
        self.deck = None
        self.players = None
        self.cardsInARound = list()

        self.setPlayers(players)
        self.setDeck(deck)
        
    def start(self):
        shuffle(self.players)
        self.deck.shuffle()
        self.dealCard()

        while self.round -1 < self.maxRound:
            print("\nround " + str(self.round))
            for player in self.players:
                self.exchangeHand(player)
            for player in self.players:
                self.takeTurn(player)
            self.printShowCards()
            self.showdown()
            self.round += 1
            self.cardsInARound = list()

    def exchangeHand(self, player):
        if player.getAlreadyExchanged():
            exchangeHand = player.getExchangeHands()
            exchangeHand.reduceCountdown()
            if exchangeHand.getCountdown() == 0:
                exchangeHand.exangeHand()

        if not player.getAlreadyExchanged():
            if player.decideWhetherToExchangeHands():
                player.setAlreadyExchanged(True)
                exchangee = player.selectAPlayer([otherPlayer for otherPlayer in self.getPlayers() if otherPlayer.getName() != player.getName()])
                exchangeHand = ExangeHands(player, exchangee)
                player.setExchangeHands(exchangeHand)


    def takeTurn(self, player):
        self.cardsInARound.append(player.takeTurn())

    def showdown(self):
        maxCard = None
        maxCardIndex = None
        for i in range(len(self.cardsInARound)):
            if (not maxCard) or (not maxCard.showdown(self.cardsInARound[i])):
                maxCard = self.cardsInARound[i]
                maxCardIndex = i
        print("Winner in this round: " + self.players[maxCardIndex].getName())
        self.players[maxCardIndex].gainPoint()

    def printShowCards(self):
        for i in range(len(self.players)):
            print(self.players[i].getName() + " shows " + self.cardsInARound[i].getSuit().name + " " + self.cardsInARound[i].getRank().name)


    def gameOver(self):
        winner = []
        maxPoint = None
        for i in range(len(self.players)):
            print(self.players[i].getName() + " got " + str(self.players[i].getPoint()) + " points! ")
            if not maxPoint or self.players[i].getPoint()>maxPoint:
                maxPoint = self.players[i].getPoint()
                winner = [self.players[i]]
            elif self.players[i].getPoint()==maxPoint:
                winner.append(self.players[i])
        print("Winner: ")
        print([player.getName() for player in winner])

    def setPlayers(self, players):
        self.players = players

    def getPlayers(self):
        return self.players

    def setDeck(self, deck):
        self.deck = deck

    def getDeck(self):
        #for card in self.deck.cards:
        #    print(card.getSuit().name, card.getRank().name)
        pass

    def dealCard(self):
        cardPerPlayer = len(self.deck.getCards()) // len(self.players)
        for i in range(cardPerPlayer):
            for player in self.players:
                player.addHand(self.deck.drawCard())
    