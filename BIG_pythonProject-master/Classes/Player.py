from DeckOfCards import *

class Player:
    def __init__(self, name, cardsNum=10):
        self.name = name
        self.hand = []
        if cardsNum>26:
            cardsNum=26
        self.cardsNum = cardsNum



    def setHand(self, deck):
        for i in range(self.cardsNum):
            self.hand.append(deck.deal_one())

P1 = Player("Eyal",10 )
deck=DeckOfCards()
P1.setHand(deck)
print(P1.hand)


