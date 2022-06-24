from Rank import Rank
from Suit import Suit


class ShowCardUtils:
    @staticmethod
    def toRank(rank):
        match rank:
            case Rank.II:
                return '2'
            case Rank.III:
                return '3'
            case Rank.IV:
                return '4'
            case Rank.V:
                return '5'
            case Rank.VI:
                return '6'
            case Rank.VII:
                return '7'
            case Rank.VIII:
                return '8'
            case Rank.IX:
                return '9'
            case Rank.X:
                return '10'
            case Rank.J:
                return 'J'
            case Rank.Q:
                return 'Q'
            case Rank.K:
                return 'K'
            case Rank.A:
                return 'A'
        

    @staticmethod
    def toSuit(suit):
        match suit:
            case Suit.CLUB:
                return '♣'
            case Suit.DIAMOND:
                return '♦'
            case Suit.HEART:
                return '♥'
            case Suit.SPADE:
                return '♠'
