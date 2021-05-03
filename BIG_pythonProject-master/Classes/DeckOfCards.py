from Card import Card
import random

class DeckOfCards:
    def __init__(self):
        self.deck = []
        for s in range(1,5):
            for v in range(1,14):
                card=Card(v,s)
                self.deck.append(card)


    def shuffle(self):
        random.shuffle(self.deck)

    def show(self):
        for i in self.deck:
            print(i)


deck = DeckOfCards()
deck.shuffle()
deck.show()

