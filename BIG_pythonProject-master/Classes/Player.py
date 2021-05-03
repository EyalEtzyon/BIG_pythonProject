from DeckOfCards import *
from Card import *

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



    def get_card(self):
        return self.hand.pop(random.randrange(0,len(self.hand)))

    def add_card(self, card):
        self.hand.append(card)


    def show(self):
        print(f"name: {self.name} hand: {self.hand}")




P1 = Player("Eyal")
deck=DeckOfCards()
P1.setHand(deck)
# print(P1.hand)
# print(P1.get_card())
# P1.add_card(Card(1,1))
P1.show()


