class ExangeHands:
    def __init__(self, exchangee, exchanger) -> None:
        self.countdown = 3
        self.exchangee = exchangee
        self.exchanger = exchanger
        self.exangeHand()
    
    def getCountdown(self):
        return self.countdown
    
    def reduceCountdown(self):
        self.countdown -= 1

    def exangeHand(self):
        temp = self.exchanger.getHand()
        self.exchanger.setHand(self.exchangee.getHand())
        self.exchangee.setHand(temp)
