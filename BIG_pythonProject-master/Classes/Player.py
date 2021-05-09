from DeckOfCards import *
from Card import *

class Player:
    #create player with name and list of cards
    def __init__(self, name, cardsNum=10):
        if type(name)!= str:
            raise TypeError("not a string")
        self.name = name
        self.hand = []
        if type(cardsNum)!= int:
            raise TypeError("not an int")
        if cardsNum>26:
            cardsNum=26
        if cardsNum<0:
            raise TypeError("cards number cant be smaller than 0")
        self.cardsNum = cardsNum

    def __repr__(self):
        return f"{self.name} {self.hand}"

    def setHand(self, deck):
        for i in range(self.cardsNum):
            self.hand.append(deck.deal_one())



    def get_card(self):
        return self.hand.pop(random.randrange(0,len(self.hand)))

    def add_card(self, card):
        self.hand.append(card)


    def show(self):
        print(f"{self.name}'s hand: {self.hand}")




# P1 = Player("Eyal")
# deck=DeckOfCards()
# P1.setHand(deck)
# # print(P1.hand)
# # print(P1.get_card())
# # P1.add_card(Card(1,1))
# P1.show()


