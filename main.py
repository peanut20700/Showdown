
from Showdown import Showdown
from Deck import Result
from HumanPlayer import HumanPlayer
from AiPlayer import AiPlayer
from Rank import Rank
from Suit import Suit
from Deck import Deck
from Card import Card

import enum

def createPlayers():
    players = list()
    humanPlayer = HumanPlayer()
    humanPlayer.nameHimself()
    players.append(humanPlayer)
    players.append(AiPlayer(1))
    players.append(AiPlayer(2))
    players.append(AiPlayer(3))
    return players

def createDeck():
    cards = list()
    for rank in Rank:
        for suit in Suit:
            card = Card()
            card.setRank(rank)
            card.setSuit(suit)
            cards.append(card)
    deck = Deck(cards)
    return deck


if __name__ == '__main__':
    players = createPlayers()
    deck = createDeck()

    showdown = Showdown(players, deck)
    #showdown.getPlayers()
    #showdown.getDeck()
    showdown.start()
    showdown.gameOver()
    '''
    for player in showdown.getPlayers():
        print("\n" + player.getName())
        for card in player.getHand():
            print(card.getSuit().name, card.getRank().name)
    '''

